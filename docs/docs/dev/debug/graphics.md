!!! tip "Tip: Testing"

    These NV2A [unit tests](https://github.com/abaire/nxdk_pgraph_tests){target=_blank} are a great way to isolate and troubleshoot graphical differences between xemu and real hardware.

    The [snapshot](../../snapshots.md) feature within xemu is another convenient way to quickly test problem areas without having to repeatedly play through large sections of a game.

    There are also other tools such as [RenderDoc]([https://renderdoc.org]){target=_blank}, [Nsight]([https://developer.nvidia.com/nsight-systems]){target=_blank}, and [nv2a-trace]([https://github.com/XboxDev/nv2a-trace]){target=_blank} which are good ways to get started into graphics debugging!


## RenderDoc

!!! tip "What is RenderDoc?"
    
    Renderdoc is a Graphical Analysis tool that can be used with xemu to capture and inspect the   emulator's GPU commands, which makes it easier to diagnose rendering bugs, or deviations from     Original Xbox hardware, this tool allows you to capture frames and analyze every draw call, texture, buffer, and shader in the frame captured.

Renderdoc is relatively easy to use, simply just [install RenderDoc]([https://renderdoc.org]){target=_blank} for your specific platform, and launch your instance of xemu through RenderDoc, by pointing it to the build or release of xemu that you would like to use in the application, once launched, you should be able to press `F12` to capture a frame of your choosing, and view the prospective capture created in the RenderDoc application.

You can also export these captures and upload them in a [GitHub issue](https://github.com/xemu-project/xemu/issues/new/choose){target=_blank} to help us track down these Graphical Bugs for fixing in the future, this is a task that is incredibly important for us to resolve Graphical Bugs in edgecase situations.

<!--
TODO:

## Nsight

TODO:

## nv2a-trace

TODO:
-->
