# Account Setup Guide

This file lists the account-only steps that should be done by the package
owner, not by the agent.

## Telegram Bot Token

1. Open Telegram and message `@BotFather`.
2. Send `/newbot`.
3. Choose a bot display name and username.
4. Copy the bot token and keep it private.
5. Do not paste the token into git-tracked files.

When Hermes is installed, configure the token with:

```bash
hermes gateway setup
hermes config set gateway.telegram.token "YOUR_BOT_TOKEN_HERE"
hermes gateway run
```

## TestPyPI

1. Register at <https://test.pypi.org/account/register/>.
2. Verify your email address.
3. Create an API token at <https://test.pypi.org/manage/account/#api-tokens>.
4. Use the token only when prompted by `twine`.

Upload command:

```bash
python -m twine upload --repository testpypi dist/*
```

Install verification command:

```bash
python -m pip install --index-url https://test.pypi.org/simple/ --no-deps hermes-textstats
```

## PyPI

1. Register at <https://pypi.org/account/register/>.
2. Verify your email address.
3. Create an API token at <https://pypi.org/manage/account/#api-tokens>.
4. Upload to real PyPI only after TestPyPI install verification passes.

Upload command:

```bash
python -m twine upload dist/*
```

## GitHub

The private repository is planned as:

```text
https://github.com/cilmar748/hermes-textstats
```

The agent can create it with GitHub CLI if `gh` remains authenticated:

```bash
gh repo create hermes-textstats --private --source . --remote origin --push
```
