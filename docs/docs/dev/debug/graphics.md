External graphics debugging tools can prove useful when trying to nail out graphical bugs or regressions, this page lists a few of the tools that are used by the xemu-project for debugging issues related to graphics.

## NV2A Unit Tests

!!! tip "What are Unit Tests?"
    
    Unit Tests are a way to compare what the emulated GPU that xemu is using to the results that you should expect via real hardware, this is an excellent method for assisting in furthering the developed of the emulated NV2A gpu that xemu uses.

The test suite is located in this [repository](https://github.com/abaire/nxdk_pgraph_tests){target=_blank}, and the associated golden results (taken from actual hardware) are located in this [repository](https://github.com/abaire/nxdk_pgraph_tests_golden_results){target=_blank}, both repositories contain instructions specific to the test that you may be trying to run, as well as information on what it takes to create new unit tests to debug other graphical issues. 


## RenderDoc

!!! tip "What is RenderDoc?"
    
    Renderdoc is a Graphical Analysis tool that can be used with xemu to capture and inspect the emulator's GPU commands, which makes it easier to diagnose rendering bugs, or deviations from Original Xbox hardware, this tool allows you to capture frames and analyze every draw call, texture, buffer, and shader in the frame captured.

RenderDoc is relatively easy to use, simply just [install RenderDoc]([https://renderdoc.org]){target=_blank} for your specific platform, and launch your instance of xemu through RenderDoc, by pointing it to the build or release of xemu that you would like to use in the application, once launched, you should be able to press `F12` to capture a frame of your choosing, and view the prospective capture created in the RenderDoc application.

You can also export these captures and upload them in a [GitHub issue]([https://github.com/xemu-project/xemu/issues/new/choose]){target=_blank} to help us track down these graphical bugs for fixing in the future, this is a task that is incredibly important for us to resolve graphical bugs in edgecase situations.

The [snapshot](../../snapshots.md) feature within xemu is another convenient way to quickly test problem areas without having to repeatedly play through large sections of a game, that can also aid in testing titles with the use of RenderDoc.

## nv2a-trace

!!! tip "What is nv2a-trace?"
    
    nv2a-trace is a graphical analysis tool developed by the organization XboxDev that is similar to apitrace, with the difference being that it targets the Xbox GPU instead of typical desktop graphics APIs.

[nv2a-trace]([https://github.com/XboxDev/nv2a-trace.git]){target=_blank} is used by connecting to an xbox using a tool called [xboxpy]([https://github.com/XboxDev/xboxpy]){target=_blank} which contains instructions on compiling and attaching to an xbox, most output will be sent to PNG files in the `out` folder, as well as a `debug.html` file being created which shows that commands that were captured.

## Nsight

!!! tip "What is Nsight?"
    
    Nvidia's Nsight tool is a graphics development tool that can allow you to debug, profile, and export frames that are built with D3D, Vulkan, OpenGL, as well as OpenVR applications.

Nsight is also relatively easy to use, simply install it for your given platform by visiting the Nsight website [here]([https://developer.nvidia.com/nsight-graphics]){target=_blank}, and installing it, once launched select `Start Activity`, and pointing it to the build or release of xemu that you would like to use in the application, and select the specific debugging activity that you would like to do.

Once the activity is selected Nsight will attach to the process, and you can capture frames as well as trace application use of GPU resources, or trace System Activity.
