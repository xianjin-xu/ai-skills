#!/usr/bin/env python3
"""获取 PR/MR 的差异文件"""

import subprocess
import sys
import json
import re
from urllib.parse import urlparse


def parse_pr_url(url):
    """解析 PR URL，提取平台、仓库、编号"""
    # GitHub: https://github.com/owner/repo/pull/123
    github_match = re.search(r"github\.com/([^/]+)/([^/]+)/pull/(\d+)", url)
    if github_match:
        return {
            "platform": "github",
            "owner": github_match.group(1),
            "repo": github_match.group(2),
            "number": github_match.group(3)
        }
    
    # GitLab: https://gitlab.com/owner/repo/-/merge_requests/456
    gitlab_match = re.search(r"gitlab\.com/([^/]+)/([^/]+)/-/(?:merge_)?requests/(\d+)", url)
    if gitlab_match:
        return {
            "platform": "gitlab",
            "owner": gitlab_match.group(1),
            "repo": gitlab_match.group(2),
            "number": gitlab_match.group(3)
        }
    
    return None


def get_github_diff(owner, repo, pr_number):
    """获取 GitHub PR 的差异"""
    try:
        # 获取 PR 信息
        pr_info = subprocess.run(
            ["gh", "pr", "view", pr_number, "--repo", f"{owner}/{repo}", "--json", 
             "title,author,baseRefName,headRefName,additions,deletions,changedFiles"],
            capture_output=True,
            text=True
        )
        pr_data = json.loads(pr_info.stdout)
        
        # 获取文件列表
        files = subprocess.run(
            ["gh", "pr", "view", pr_number, "--repo", f"{owner}/{repo}", "--json", "files"],
            capture_output=True,
            text=True
        )
        files_data = json.loads(files.stdout)
        
        return {
            "success": True,
            "pr": pr_data,
            "files": files_data.get("files", [])
        }
    except subprocess.CalledProcessError as e:
        return {"success": False, "error": e.stderr}
    except Exception as e:
        return {"success": False, "error": str(e)}


def get_gitlab_diff(owner, repo, mr_number):
    """获取 GitLab MR 的差异"""
    try:
        # 获取 MR 信息
        mr_info = subprocess.run(
            ["glab", "mr", "view", mr_number, "--repo", f"{owner}/{repo}", "--output", "json"],
            capture_output=True,
            text=True
        )
        mr_data = json.loads(mr_info.stdout)
        
        # 获取文件列表
        files = subprocess.run(
            ["glab", "mr", "view", mr_number, "--repo", f"{owner}/{repo}", " --output", "json"],
            capture_output=True,
            text=True
        )
        
        return {
            "success": True,
            "mr": mr_data,
            "files": []
        }
    except subprocess.CalledProcessError as e:
        return {"success": False, "error": e.stderr}
    except Exception as e:
        return {"success": False, "error": str(e)}


def get_diff(url):
    """根据 URL 获取差异"""
    parsed = parse_pr_url(url)
    if not parsed:
        return {"success": False, "error": "无法解析 URL"}
    
    if parsed["platform"] == "github":
        return get_github_diff(parsed["owner"], parsed["repo"], parsed["number"])
    else:
        return get_gitlab_diff(parsed["owner"], parsed["repo"], parsed["number"])


if __name__ == "__main__":
    url = sys.argv[1] if len(sys.argv) > 1 else ""
    if not url:
        print("Usage: python pr_diff.py <pr_url>")
        sys.exit(1)
    
    result = get_diff(url)
    print(json.dumps(result, indent=2, ensure_ascii=False))