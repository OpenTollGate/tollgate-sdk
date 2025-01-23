You need golang.mk because it takes care of the cross‐compilation
environment for Go under OpenWrt. It sets up the correct GOARCH, GOOS,
GOMIPS, and GOARM values based on the SDK’s target configuration,
ensures the right compiler flags get used, and applies various OpenWrt
patches/quirks that let Go interoperate with the OpenWrt build
system. Without golang.mk, you would have to manually replicate all of
that logic and risk mismatches between your host and target builds.

In your Makefile, you currently hardcode “GOOS=linux GOARCH=arm64” for the Build/Compile step:
  
GOOS=linux \
GOARCH=arm64 \
GOARM=$(GO_ARM) \
GOMIPS=$(GO_MIPS) \
GO386=$(GO_386) \
 …

That works fine for the GL-MT3000 (which is an ARM64 device) but
breaks on the GL-AR300m (which is a 32-bit MIPS). When you try
building for the GL-AR300m, it still sets GOARCH=arm64, causing the
“_check_for_64_bit_pointer_matching_GoInt is negative” error.

Below are some suggestions to fix it:

1. Let golang.mk detect the architecture instead of forcing it. That
means removing or changing lines like GOARCH=arm64 so that they become
something like:
  
GOOS=$(GO_TARGET_OS) \
GOARCH=$(GO_TARGET_ARCH) \
GOARM=$(GO_ARM) \
GOMIPS=$(GO_MIPS) \
GO386=$(GO_386) \
…

2. Check that golang.mk knows how to convert ath79 (or mips_24kc) into
GOARCH=mips. In older OpenWrt versions (or custom golang.mk), the
variable expansions for GO_TARGET_ARCH might not handle mips_24kc
properly. Make sure that the line:

GO_TARGET_ARCH:=$(subst aarch64,arm64,$(subst x86_64,amd64,$(subst i386,386,$(ARCH))))

also handles mips or mips_24kc. If it doesn’t, add something like:

GO_TARGET_ARCH:=$(subst mips_24kc,mips,$(subst ... ))

so it can pick up the correct architecture.

3. Confirm that your OpenWrt .config has the needed CONFIG_mips or
target-ath79 flags so that golang.mk knows it’s compiling for MIPS.

4. Make sure your package’s Makefile and your build scripts don’t
override local environment variables that might conflict with
golang.mk. Let golang.mk do all the detection and cross‐compilation
setup.

In summary, you need golang.mk so that Go cross‐compiles properly to
the various OpenWrt targets. You simply have to remove or fix any
hardcoded GOARCH/GOOS lines and ensure golang.mk converts your ath79
(mips_24kc) target into GOARCH=mips and the right
GOMIPS/hardfloat/softfloat settings. That should resolve the “64 bit
pointer” build error for the GL-AR300m.