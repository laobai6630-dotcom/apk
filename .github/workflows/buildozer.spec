[app]

# (str) 应用标题
title = 试题提取工具

# (str) 包名
package.name = tiquqi

# (str) 域名（包名反转前缀）
package.domain = org.yh

# (str) 源代码所在目录
source.dir = .

# (list) 包含的文件后缀
source.include_exts = py,png,jpg,kv,atlas,keystore,ttf

# (str) 版本号
version = 1.0

# (list) 核心依赖库 (根据您的代码需求)
requirements = python3,kivy,openpyxl,python-docx

# (str) 屏幕方向
orientation = portrait

# -----------------------------------------------------------------------------
# 安卓特有设置
# -----------------------------------------------------------------------------

# (list) 权限申请：适配安卓11+的文件管理逻辑
android.permissions = READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, MANAGE_EXTERNAL_STORAGE

# (int) 目标 API 级别（建议 31 或 33）
android.api = 31

# (int) 最低支持 API
android.minapi = 21

# (bool) 是否允许存储在 SD 卡
android.allow_backup = True

# (str) 架构支持
android.archs = arm64-v8a, armeabi-v7a

# -----------------------------------------------------------------------------
# 证书签名设置 (正式打包关键)
# -----------------------------------------------------------------------------

# (str) 证书文件名 (确保该文件与 buildozer.spec 在同一文件夹)
android.keystore = my-release-key.keystore

# (str) 证书口令
android.keystore_password = 004063

# (str) 证书别名 (您之前命令生成的别名)
android.keyalias = my-key-alias

# (str) 别名口令
android.keyalias_password = 004063

# -----------------------------------------------------------------------------
# 打包编译设置
# -----------------------------------------------------------------------------

[buildozer]

# (int) 日志级别 (0 = 仅错误, 1 = 信息, 2 = 调试)
log_level = 2

# (int) 发生错误时是否停止
warn_on_root = 1