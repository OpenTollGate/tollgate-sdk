The error you're encountering:

```
ninja: error: unknown target 'install'
make[2]: *** [Makefile:95: /tmp/openwrt-sdk/.../.built] Error 1
ERROR: package/helloworld failed to build.
```

occurs because the `ninja` build system doesn't have an `install` target defined in your `CMakeLists.txt`. When using OpenWrt's build system with CMake (`include $(INCLUDE_DIR)/cmake.mk`), it expects the build system to provide an `install` target that correctly installs the built files into a staging area. Since this target is missing, the build process fails.

### **Solution: Add an Install Target to Your `CMakeLists.txt`**

You need to define the installation rules in your `CMakeLists.txt` so that `ninja install` knows what to do. Here's how to modify your `src/CMakeLists.txt`:

#### **Modify `src/CMakeLists.txt`**

```cmake
cmake_minimum_required(VERSION 3.0)
project(helloworld CXX)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(helloworld helloworld.cpp)

# Add install directive
install(TARGETS helloworld DESTINATION bin)
```

- **Explanation**:
  - `install(TARGETS helloworld DESTINATION bin)` tells CMake to install the `helloworld` executable to the `bin` directory. In the context of OpenWrt, this typically corresponds to `/usr/bin` on the target device.
  - This addition creates an `install` target for `ninja`, allowing `ninja install` to execute successfully.

#### **Ensure Proper Use of `cmake.mk` in Your Package Makefile**

Since you're using `cmake.mk`, the build and installation process is managed by the CMake build system. You don't need to manually define installation steps in your OpenWrt package `Makefile`. In fact, doing so can cause conflicts or redundant actions.

#### **Update Your Package `Makefile`**

Here's how your `Makefile` should look after the adjustments:

```makefile
include $(TOPDIR)/rules.mk

# Package metadata
PKG_NAME:=helloworld
PKG_VERSION:=1.0
PKG_RELEASE:=1
PKG_SOURCE_URL:=https://github.com/nicanor-romero/openwrt_helloworld.git
PKG_SOURCE_BRANCH:=github/master
PKG_SOURCE_PROTO:=git
PKG_SOURCE:=$(PKG_NAME)-$(PKG_VERSION).tar.xz
PKG_SOURCE_SUBDIR:=$(PKG_NAME)-$(PKG_VERSION).$(PKG_RELEASE)
PKG_SOURCE_VERSION:=6af999d4248592b7d73c1acecbe687baf2bd0990
PKG_BUILD_DIR:=$(BUILD_DIR)/$(PKG_SOURCE_SUBDIR)

include $(INCLUDE_DIR)/package.mk
include $(INCLUDE_DIR)/cmake.mk

# Package definition
define Package/helloworld
  SECTION:=utils
  CATEGORY:=Utilities
  TITLE:=Helloworld -- prints a snarky message
  DEPENDS:=+libstdcpp +libpthread +librt +libgcc
endef

define Package/helloworld/description
  Simple helloworld program for OpenWrt.
endef

# Compilation and linking flags
TARGET_CXXFLAGS += -fno-rtti
TARGET_LDFLAGS += -lgcc_s -lstdc++ -lm

# CMake options
CMAKE_OPTIONS += \
    -DCMAKE_CXX_FLAGS="$(TARGET_CXXFLAGS)" \
    -DCMAKE_EXE_LINKER_FLAGS="$(TARGET_LDFLAGS)" \
    -DCMAKE_BUILD_TYPE=Release

define Build/Prepare
	mkdir -p $(PKG_BUILD_DIR)
	$(CP) ./src/* $(PKG_BUILD_DIR)/
endef

# Remove custom install steps if any
#undefine Package/helloworld/install
#endef

$(eval $(call BuildPackage,$(PKG_NAME)))
```

- **Explanation**:
  - **Removed Custom Install Commands**: By default, `cmake.mk` handles the installation process using the `install` target defined in `CMakeLists.txt`. Remove or comment out any custom `define Package/helloworld/install` sections to avoid conflicts.
  - **Kept Build Preparation**: The `Build/Prepare` section copies your source files to the build directory, which is fine to keep.

### **Final Steps**

1. **Clean the Build Environment**:

   It's essential to clean the previous build artifacts to ensure that the new changes take effect.

   ```bash
   make package/helloworld/{clean,clean-build}
   ```

2. **Build the Package with Verbose Output**:

   This allows you to see the detailed build steps and confirm that the `install` target is being called correctly.

   ```bash
   make package/helloworld/{compile,install} V=s
   ```

3. **Check for Successful Build and Install**:

   The build process should now complete without the previous error. Look for confirmation messages indicating that the `helloworld` binary has been installed to the correct staging directory.

### **Explanation of the Error**

- **Why the Error Occurred**:

  The OpenWrt build system relies on the package's build system (in this case, CMake) to handle installation into a staging directory. When it runs `ninja install`, it expects an `install` target defined in your `CMakeLists.txt`. Since this target wasn't defined, `ninja` failed with the error `unknown target 'install'`.

- **Role of `cmake.mk`**:

  The inclusion of `cmake.mk` in your package `Makefile` automatically sets up the build and install steps using CMake and Ninja. It expects standard CMake targets like `all` and `install` to be available.

### **Additional Notes**

- **Consistency Between Build and Install**:

  By defining the install steps in `CMakeLists.txt`, you ensure that the build and install processes are aligned and managed by CMake, reducing the risk of errors.

- **Custom Installation Paths**:

  If you need to install files to locations other than `bin`, you can adjust the `DESTINATION` in the `install` command accordingly.

  ```cmake
  install(TARGETS helloworld DESTINATION sbin)
  ```

- **Dependencies and Linking**:

  Ensure that all required libraries are correctly specified in your `DEPENDS` and linked in your build configuration. This avoids runtime errors related to missing libraries.

- **Verbose Build Output**:

  Using the `V=s` or `V=99` flag when building provides detailed output, which is invaluable for troubleshooting.

### **References for Future Issues**

- **OpenWrt Build System Documentation**:

  Refer to the [OpenWrt Build System – Build System Usage](https://openwrt.org/docs/guide-developer/build-system/use-buildsystem) for detailed information on package creation and troubleshooting.

- **CMake Documentation**:

  The [CMake Install Documentation](https://cmake.org/cmake/help/latest/command/install.html) provides comprehensive guidance on how to define installation rules.

### **Conclusion**

By adding the `install` directive to your `CMakeLists.txt` and allowing `cmake.mk` to handle the installation process, you resolve the `unknown target 'install'` error. This aligns your build and install steps with the expectations of the OpenWrt build system, leading to a successful package build.

---

Feel free to ask if you have any further questions or need additional assistance!