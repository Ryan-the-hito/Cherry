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
- 当 Cherry 能够正常运行时，它将在 menubar 中静静等候点击。
- 点击“Manage my volume!”，终端将弹出两个窗口，这是正常现象，不必担心。随后两个窗口将依次最小化，Cherry 的主界面将出现在屏幕中间。（在运行软件时请保持终端软件在后台运行，不要关闭。）
- 在第一行的选框中选择你正在用来听的设备——注意，不是选择输出设备，而是用户用来听见声音的设备。
- 在第二行的两个空格中可以填入你最舒适的声压范围。软件已经默认填写了一个对人耳友好的区间，用户可以随时更改这一数值，Cherry 会实时响应。如果您不清楚自己适合何种声压范围，可以参考下面这张图。对于使用耳机和扬声器等不同设备，这一取值可能有变化。如果您使用耳机，可以尽量将声压值降低一些。
- 当上述设置都完成后，点击“Start”，Cherry 就会灵活地调整音量大小了。界面上将显示两个数值。第一个数值是系统音量的数值，在 Cherry 的调节下，它将实时变动。第二个数值是分贝值，它是原输入音频的实际分贝值，如果您的配置一切正确，您将看到它鲜活但不规律地跳动着。这就是即将输到您鼓膜的声音数据，它将在第一行所示的音量调节的辅助下，变得更加柔和。
- 如果您想停止使用 Cherry，先点击 “Stop”，这时音量会切换到 1，保证您的耳朵不会收到冲击，随后您可以点击左上角的“❎”，关闭窗口。这时 Cherry 的主界面就不会在前台运行了，您可以关闭终端的窗口。
- 主界面关闭后，Cherry 还将在 menubar 中等待点击，如果您需要完全退出，只需点击 menubar 中的图标，选择“Quit”即可。
- 如果您需要恢复对音量的控制，请在系统设置或右上角的控制中心中切换声道即可。下次使用 Cherry 时还需提前切换声道。

![声压变化图](https://github.com/Ryan-the-hito/Cherry/blob/main/image/acoustic%20pressure%20range.webp)

## 🤔问题检查：

### 问题 1：第一行 value 没动静，第二行 dB 也没动静：麦克风权限错误

- 说明 Cherry 没有收到来自系统的声音信息。
- 请打开系统设置看看是否开启了麦克风权限。
- 如果 Cherry 没有显示在麦克风权限的列表中，请使用以下代码，复制进入终端后执行，输入密码，即可在列表中见到 Cherry：

`sudo sqlite3 ~/Library/Application\ Support/com.apple.TCC/TCC.db "INSERT or REPLACE INTO access VALUES('kTCCServiceMicrophone','org.pythonmac.unspecified.Cherry',0,0,4,1,NULL,NULL,0,'UNUSED',NULL,0,1622199671);"`

### 问题 2：第一行 value 没动静或者缩至最小值，第二行 dB 却有动静：输入设备（声道）选择错误

- 说明 Cherry 收到了系统音频数据，但是这个输入的设备是有误的，往往选择了自带的麦克风作为输入设备，而没有选择 BlackHole 2ch。
- 如果选择了 BlackHole 2ch 仍然出现了上述现象，说明是系统迟钝的问题。这个问题我自己也偶尔遇到，就像切换输入法的时候，图标改变了，但实际的输入法还是没有切换过来一样，macOS 在一些切换上确实是比较迟钝的，这就是为什么必须在打开 Cherry 之前先设置好声道。如果遇到这种情况，请重新切换一下声道，然后重启 Cherry 即可。

### 问题3：两行都有动静，但声音却没有变化：Accessibility 权限错误

- 这说明 Cherry 收到了声音信息，但是却无法对系统设置发号施令，大概是没有打开辅助功能的权限。
- 请打开系统设置，在相应的权限版块勾选 Cherry，重启 Cherry 即可。

### 其他情况：

- 请打开 Cherry 的全磁盘权限（Full Disk Access）
- 请保证终端设备（Terminal）和 Cherry 一样拥有 Accessibbility、Microphone 和 Full Disk Access 的权限。
