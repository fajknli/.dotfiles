好的，我把从项目开始到发布 v0.4.0 的所有**代码之外的操作**整理成一份速查手册，以后你随时可以翻。

---

## PalaceLite 开发与发布速查手册

### 一、环境准备

```bash
# 创建虚拟环境
python -m venv venv
source venv/bin/activate

# 安装开发依赖
pip install -e .
pip install black isort pytest build twine
```

### 二、代码格式化

```bash
# 格式化代码
black palacelite/ scripts/
isort palacelite/ scripts/
```

### 三、版本号管理

需要同步修改两个文件：
```bash
# palacelite/__init__.py
__version__ = "0.4.0"

# pyproject.toml
version = "0.4.0"
```

开发中可以用 `0.5.0.dev0`，发布时去掉 `.dev0`。

### 四、提交与打 Tag

```bash
# 提交
git add -A
git commit -m "Release v0.4.0: 简短描述"

# 打 tag
git tag v0.4.0

# 推送
git push
git push --tags
```

**注意**：tag 一旦推送，**绝不能**用 `amend` 或 `force push` 修改 tag 指向的 commit。有问题发新版本。

### 五、构建与检查

```bash
# 清理旧构建
rm -rf dist/ build/ *.egg-info palacelite.egg-info/

# 构建
python -m build

# 检查包是否合规
twine check dist/*
```

### 六、发布到 PyPI

```bash
# 上传
twine upload dist/*
```

**注意**：PyPI **不允许**覆盖已上传的同版本文件。如果 README 写错了，只能发新版本（如 v0.4.1）。

### 七、本地测试发布的包

```bash
# 创建临时虚拟环境
python -m venv /tmp/test_palacelite
source /tmp/test_palacelite/bin/activate

# 安装并测试
pip install palacelite
palacelite --help
```

### 八、GitHub Release

1. 打开 `https://github.com/fajknli/palacelite/releases`
2. 点击「Create a new release」
3. 选择 tag（如 `v0.4.0`）
4. 标题写版本号，内容复制 CHANGELOG 对应部分
5. 发布

### 九、Git 历史整理（开发中）

```bash
# 把当前改动合并到上一个 commit，不改 commit message
git add .
git commit --amend --no-edit

# 安全地强制推送
git push --force-with-lease
```

**只在开发分支用，打了 tag 的 commit 绝不能动。**

### 十、可选依赖

`pyproject.toml` 中配置：
```toml
[project.optional-dependencies]
chat = ["llama-cpp-python>=0.3.0"]
```

用户安装：`pip install palacelite[chat]`

### 十一、常用命令速查

| 操作 | 命令 |
|------|------|
| 格式化 | `black . && isort .` |
| 构建 | `rm -rf dist/ && python -m build` |
| 检查包 | `twine check dist/*` |
| 上传 | `twine upload dist/*` |
| 打 tag | `git tag v0.4.0 && git push --tags` |
| 整理提交 | `git commit --amend --no-edit && git push --force-with-lease` |

---

这份手册覆盖了从开发到发布的全部非代码操作。以后忘了直接翻这个。
