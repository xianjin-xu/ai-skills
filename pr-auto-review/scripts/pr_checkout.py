#!/usr/bin/env python3
"""拉取 PR/MR 到本地临时分支"""

import subprocess
import sys
import json
import re


def parse_pr_url(url):
    """解析 PR URL"""
    github_match = re.search(r"github\.com/([^/]+)/([^/]+)/pull/(\d+)", url)
    if github_match:
        return {
            "platform": "github",
            "owner": github_match.group(1),
            "repo": github_match.group(2),
            "number": github_match.group(3)
        }
    
    gitlab_match = re.search(r"gitlab\.com/([^/]+)/([^/]+)/-/(?:merge_)?requests/(\d+)", url)
    if gitlab_match:
        return {
            "platform": "gitlab",
            "owner": gitlab_match.group(1),
            "repo": gitlab_match.group(2),
            "number": gitlab_match.group(3)
        }
    
    return None


def checkout_github_pr(owner, repo, pr_number):
    """拉取 GitHub PR 到本地临时分支"""
    branch_name = f"pr/{pr_number}"
    
    try:
        # 方法1: 使用 gh pr checkout
        result = subprocess.run(
            ["gh", "pr", "checkout", pr_number, "--repo", f"{owner}/{repo}", "--branch", branch_name],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            return {"success": True, "branch": branch_name, "message": result.stdout}
        
        # 方法2: 手动拉取
        subprocess.run(
            ["git", "fetch", "origin", f"pull/{pr_number}/head:{branch_name}"],
            capture_output=True,
            text=True
        )
        subprocess.run(
            ["git", "checkout", branch_name],
            capture_output=True,
            text=True
        )
        
        return {"success": True, "branch": branch_name, "message": f"Checked out to branch: {branch_name}"}
    except Exception as e:
        return {"success": False, "error": str(e)}


def checkout_gitlab_mr(owner, repo, mr_number):
    """拉取 GitLab MR 到本地临时分支"""
    branch_name = f"mr/{mr_number}"
    
    try:
        result = subprocess.run(
            ["glab", "mr", "checkout", mr_number, "--repo", f"{owner}/{repo}", "--branch", branch_name],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            return {"success": True, "branch": branch_name, "message": result.stdout}
        
        return {"success": False, "error": result.stderr}
    except Exception as e:
        return {"success": False, "error": str(e)}


def checkout(url):
    """拉取 PR/MR"""
    parsed = parse_pr_url(url)
    if not parsed:
        return {"success": False, "error": "无法解析 URL"}
    
    if parsed["platform"] == "github":
        return checkout_github_pr(parsed["owner"], parsed["repo"], parsed["number"])
    else:
        return checkout_gitlab_mr(parsed["owner"], parsed["repo"], parsed["number"])


if __name__ == "__main__":
    url = sys.argv[1] if len(sys.argv) > 1 else ""
    if not url:
        print("Usage: python pr_checkout.py <pr_url>")
        sys.exit(1)
    
    result = checkout(url)
    print(json.dumps(result, indent=2, ensure_ascii=False))