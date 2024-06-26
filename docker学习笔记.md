# Docker 学习笔记

## 什么是 Docker 和容器

Docker 是一种容器化技术。要理解 Docker，首先需要理解什么是容器。

根据官方的定义，容器是一系列与系统其他部分隔离开的进程，这些进程从一个镜像运行，并由该镜像提供支持所需的全部文件。容器中的镜像包含了应用的所有依赖项，因此在开发、测试和生产的整个过程中，它都具有可移植性和一致性。

## 理解容器的类比

这个概念可能一开始不太好理解，所以我们用一个例子来说明。

### 做饭的类比

假设我们把开发的程序比作做饭，不同的菜肴需要不同的食材和厨具：

- **炒菜** 需要炒锅和食材
- **炖汤** 需要汤锅和食材
- **烧肉** 需要烤箱和食材

现在，假设有三个人：
- **A** 只需要吃炒菜
- **B** 只需要喝汤
- **C** 只需要吃烧肉

如果要满足三个人的需求，我们是否需要为每个人提供一整套完整的食材和厨具呢？显然不需要。

### 容器的作用

容器的作用类似于将每个人所需的东西打包放在一起，满足他们的需求，这样可以节省大量的空间和资源。例如：

- 为 **A** 提供炒锅和炒菜的食材
- 为 **B** 提供汤锅和炖汤的食材
- 为 **C** 提供烤箱和烧肉的食材

这种方式使得资源分配更加高效，就像容器技术使应用的依赖打包在一起，从而提高资源利用率并确保应用在不同环境中的一致性和可移植性。

## docker的使用1--启动MySQL容器
![](https://github.com/whu-ljy/2024_training/blob/4570904840f90e8e6feea88e23077f000c8ac424/120dcc53e504bc3d1f244c0b8960c6ee.png)

### 常规的增删改查
![](https://github.com/whu-ljy/2024_training/blob/7dc5f4e13ed29f23e5a372c5646e80f9cc81af0c/c003b9a2336b0a2dfaed9576b6736a15.png)

## docker的使用2--redis的增删改查
![](https://github.com/whu-ljy/2024_training/blob/6644a739d92556f4b2e359173254788f6a6d996b/%E5%9B%BE%E7%89%87%E5%90%88%E9%9B%86/Redis%E5%A2%9E%E5%88%A0%E6%94%B9%E6%9F%A5%E5%9B%BE%E7%89%87.png)

