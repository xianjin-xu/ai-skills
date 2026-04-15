#!/usr/bin/env python3
"""验证 GitHub/GitLab CLI 登录状态"""

import subprocess
import sys
import json


def check_github_auth():
    """检查 GitHub CLI 登录状态"""
    try:
        result = subprocess.run(
            ["gh", "auth", "status"],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            data = json.loads(result.stdout)
            return {"logged_in": True, "user": data.get("user", "unknown"), "scopes": data.get("scopes", [])}
        else:
            return {"logged_in": False, "message": result.stderr}
    except FileNotFoundError:
        return {"logged_in": False, "message": "gh CLI not found. Please install: https://cli.github.com"}
    except Exception as e:
        return {"logged_in": False, "message": str(e)}


def check_gitlab_auth():
    """检查 GitLab CLI 登录状态"""
    try:
        result = subprocess.run(
            ["glab", "auth", "status"],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            return {"logged_in": True, "message": result.stdout}
        else:
            return {"logged_in": False, "message": result.stderr}
    except FileNotFoundError:
        return {"logged_in": False, "message": "glab CLI not found. Please install: https://gitlab.com/gitlab-org/cli"}
    except Exception as e:
        return {"logged_in": False, "message": str(e)}


if __name__ == "__main__":
    platform = sys.argv[1] if len(sys.argv) > 1 else "github"
    
    if platform == "github":
        result = check_github_auth()
    else:
        result = check_gitlab_auth()
    
    print(json.dumps(result, indent=2, ensure_ascii=False))