# 🍒Cherry: Make your volume change softer

![Title](https://github.com/Ryan-the-hito/Cherry/blob/main/image/Cherry_Title.png)

## ⚙️使用方法：

### 第 1 步：安装 BlackHole

- [下载并安装 BlackHole 2ch](https://github.com/Ryan-the-hito/Cherry/blob/main/BlackHolePKG/BlackHole2ch.v0.4.0.pkg)，安装后在音量控制中心会看到一个名为 BlackHole 2ch 的新的输入输出设备。
- BlackHole 是一个开源的 macOS 虚拟音频引擎，它可以联通系统声道，让一个软件访问其他软件的声音输出，其开源地址[在这里](https://github.com/ExistentialAudio/BlackHole)。
- Cherry 需要这个插件，才能实时地获取电脑音量，并做出调整。

### 第 2 步：下载 device-volume-adjuster

- [下载 device-volume-adjuster](https://github.com/jonomuller/device-volume-adjuster/releases/download/v1.0.0/AdjustVolume.zip)，下载后将压缩包解压，打开 Finder（访达），把其中的命令文件拷贝到`/usr/local/bin`路径下。（这是一个隐藏文件夹，需要首先让所有文件夹可见。另外，移动该文件夹内的文件需要输入密码或使用 TouchID 解锁）
- device-volume-adjuster 是专为 macOS 设计的音量调节命令行工具，它也是完全开源和安全的，其开源地址[在此](https://github.com/jonomuller/device-volume-adjuster)。
- Cherry 需要这个命令行工具，才能调节电脑的音量高低。

### 第 3 步：配置声道

- 在 macOS 上打开 Audio MIDl Setup，点击左下角的“➕”号，点击创建“多输出设备”（Create Multi-Output Device），将你最常使用的音频输出设备勾选上，最后再把 BlackHole 2ch 勾选上。
- 把自己常用设备勾选上是为了在这个声道内听到声音，勾选 BlackHole 2ch 是为了让 Cherry 能够收到来自设备的音频数据。这样就可以边听到声音，边将声音信号传递给 Cherry 了。

### 第 4 步：选择当前声道

- 配置好声道后，打开 System Preferences，将当前的输出设备（Output）设置为刚才配置好的多输出设备，将当前的输入设备（Input）设置为“BlackHole 2ch”。
- 只有选对了声道，Cherry 才能正确无误地运行，因此**每次使用 Cherry 前都必须设置一次声道**（第 1、2、3 步都只需做一次即可，选择声道这一步骤必须在每次使用 Cherry 前都检查一次）。

### 第 5 步：下载、打开 Cherry 和授予权限

- 从 Releases 里下载 Cherry 的安装包后，解压，移动到 Applications 文件夹中。
- 点击图标，启动软件，将弹出权限弹窗，请为 Cherry 提供 Accessibbility、Microphone、Full Disk Access 和 Automation 四组权限。
- 由于 Cherry 和其他任何我做的软件一样，都不联网，所以用户尽可以提供上述权限，而不必担心网络攻击或隐私泄漏的问题。
- Cherry 需要获取上述权限，才能真正在系统上自如地运行。

### 第 6 步：使用 Cherry

- 第一次运行时，如果没有合适的授权，可能会发生错误，这时候可以重启一下 Cherry，如果发现授权不完整，或者运行不正常，请移步问题检查部分。
- 当 Cherry 能够正常运行时，它将在 menu bar 中静静等候点击。
- 点击“Manage my volume!”，终端将弹出两个窗口，这是正常现象，不必担心。随后两个窗口将依次最小化，Cherry 的主界面将出现在屏幕中间。
- 在第一行的选框中选择你正在用来听的设备——注意，不是选择输出设备，而是用户

- 点击“Manage my volume!”，终端将弹出两个窗口，这是正常现象，不必担心。随后两个窗口将依次最小化，Cherry 的主界面将出现在屏幕中间。
