#!/usr/bin/env python3
"""纯 git 命令拉取 PR/MR 到本地临时分支"""

import subprocess
import sys
import json
import re
import os


def parse_pr_url(url):
    """解析 PR URL，提取仓库路径和 PR 编号"""
    # GitHub: https://github.com/owner/repo/pull/123
    github_match = re.search(r"github\.com/([^/]+)/([^/]+)/pull/(\d+)", url)
    if github_match:
        return {
            "platform": "github",
            "owner": github_match.group(1),
            "repo": github_match.group(2),
            "number": github_match.group(3)
        }

    # GitHub with merge_requests path
    github_match2 = re.search(r"github\.com/([^/]+)/([^/]+)/-/merge_requests/(\d+)", url)
    if github_match2:
        return {
            "platform": "github",
            "owner": github_match2.group(1),
            "repo": github_match2.group(2),
            "number": github_match2.group(3)
        }

    # GitLab: https://gitlab.com/owner/repo/-/merge_requests/456
    gitlab_match = re.search(r"gitlab[^/]*/([^/]+)/([^/]+)/-/(?:merge_)?requests/(\d+)", url)
    if gitlab_match:
        return {
            "platform": "gitlab",
            "owner": gitlab_match.group(1),
            "repo": gitlab_match.group(2),
            "number": gitlab_match.group(3)
        }

    return None


def get_remote_url(owner, repo):
    """获取 remote URL，可能需要组合"""
    # 尝试从现有 remote 获取
    try:
        result = subprocess.run(
            ["git", "remote", "get-url", "origin"],
            capture_output=True,
            text=True,
            cwd=os.getcwd()
        )
        if result.returncode == 0:
            return result.stdout.strip()
    except Exception:
        pass
    
    # 尝试从 upstream 获取
    try:
        result = subprocess.run(
            ["git", "remote", "get-url", "upstream"],
            capture_output=True,
            text=True,
            cwd=os.getcwd()
        )
        if result.returncode == 0:
            return result.stdout.strip()
    except Exception:
        pass
    
    return f"https://github.com/{owner}/{repo}.git"


def checkout_pr(url, branch_prefix="pr"):
    """拉取 PR/MR 到本地临时分支"""
    parsed = parse_pr_url(url)
    if not parsed:
        return {"success": False, "error": "无法解析 URL"}

    number = parsed["number"]
    platform = parsed["platform"]
    owner = parsed["owner"]
    repo = parsed["repo"]

    branch_name = f"{branch_prefix}/{number}"

    try:
        if platform == "github":
            ref = f"pull/{number}/head"
        else:
            ref = f"merge-requests/{number}/head"

        # Fetch PR branch
        fetch_result = subprocess.run(
            ["git", "fetch", "origin", f"{ref}:{branch_name}"],
            capture_output=True,
            text=True
        )

        if fetch_result.returncode != 0:
            # 尝试 GitLab 格式
            fetch_result = subprocess.run(
                ["git", "fetch", "origin", f"merge-requests/{number}/head:{branch_name}"],
                capture_output=True,
                text=True
            )

        if fetch_result.returncode != 0:
            return {"success": False, "error": fetch_result.stderr}

        # Checkout to branch
        checkout_result = subprocess.run(
            ["git", "checkout", branch_name],
            capture_output=True,
            text=True
        )

        if checkout_result.returncode != 0:
            return {"success": False, "error": checkout_result.stderr}

        return {
            "success": True,
            "branch": branch_name,
            "platform": platform,
            "number": number,
            "owner": owner,
            "repo": repo,
            "message": f"Checked out to branch: {branch_name}"
        }

    except Exception as e:
        return {"success": False, "error": str(e)}


def get_diff(base_branch="main"):
    """获取当前分支相对于基础分支的变更"""
    try:
        # 获取变更的文件列表
        files_result = subprocess.run(
            ["git", "diff", f"{base_branch}..HEAD", "--name-only"],
            capture_output=True,
            text=True
        )

        # 获取完整的 diff
        diff_result = subprocess.run(
            ["git", "diff", f"{base_branch}...HEAD"],
            capture_output=True,
            text=True
        )

        return {
            "success": True,
            "files": files_result.stdout.strip().split("\n") if files_result.stdout.strip() else [],
            "diff": diff_result.stdout
        }
    except Exception as e:
        return {"success": False, "error": str(e)}


if __name__ == "__main__":
    url = sys.argv[1] if len(sys.argv) > 1 else ""
    if not url:
        print("Usage: python git_pr_checkout.py <pr_url>")
        sys.exit(1)

    result = checkout_pr(url)
    print(json.dumps(result, indent=2, ensure_ascii=False))