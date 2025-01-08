It appears that the issue you're encountering stems from a mismatch in exception handling settings between your code and the standard libraries provided by the OpenWrt toolchain. The `_Unwind_Resume` symbol is part of the GCC exception handling mechanism, and if exceptions are disabled in your code but required by the standard library, you'll encounter undefined reference errors.

Here's how you can resolve the error:

### **1. Enable Exceptions in Your Compilation Flags**

Even if your code doesn't explicitly use exceptions, the C++ Standard Library (`libstdc++`) may use them internally. Disabling exceptions in your compilation flags can lead to missing symbols during linking.

**Modify your `Makefile` to remove `-fno-exceptions`:**

```makefile
# Remove -fno-exceptions
TARGET_CXXFLAGS += -fno-rtti
```

### **2. Remove Static Linking Flags**

Static linking of standard libraries can cause symbol resolution issues, especially for exception handling symbols. Ensure you're linking against shared libraries provided by the toolchain.

**Update your `TARGET_LDFLAGS` by removing `-static` flags:**

```makefile
# Remove -static and -static-libstdc++ -static-libgcc
TARGET_LDFLAGS += -lstdc++ -lgcc_s -lm
```

### **3. Ensure Proper Linking Order and Libraries**

The order in which libraries are linked can affect symbol resolution.

**Modify your `CMakeLists.txt` to ensure proper linking:**

```cmake
cmake_minimum_required(VERSION 3.0)
project(helloworld CXX)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(helloworld helloworld.cpp)

# Link against standard libraries
target_link_libraries(helloworld
    stdc++
    gcc_s
    m
    pthread
    rt
)

# Ensure proper compiler and linker flags are applied
set_target_properties(helloworld PROPERTIES
    COMPILE_FLAGS "${CMAKE_CXX_FLAGS}"
    LINK_FLAGS "${CMAKE_EXE_LINKER_FLAGS}"
)
```

### **4. Clean and Rebuild Your Package**

Old object files may still have the previous settings. It's crucial to perform a clean build.

**Run the following commands:**

```bash
# Clean the build directory
make package/helloworld/clean

# Compile with verbose output to see all compiler and linker flags
make package/helloworld/compile V=s
```

### **5. Verify Toolchain Compatibility**

Ensure that your OpenWrt SDK and toolchain are up-to-date and consistent.

- **Check GCC Version:** Confirm that the GCC version used by the toolchain matches the one expected by your package.
- **Rebuild Toolchain (if necessary):** If there's a mismatch, consider rebuilding the toolchain to ensure compatibility.

### **6. Avoid Mixing Different Exception Handling Models**

Mixing code or libraries compiled with different exception handling models (e.g., DWARF-2 vs. SJLJ) can cause `_Unwind_Resume` errors.

- **Ensure Consistent Exception Handling:** All code and libraries should be compiled with the same exception handling settings.

### **7. Verify Library Availability**

Ensure that the required libraries are available in the toolchain's staging directory.

- **Check for `libgcc_s`:** Verify that `libgcc_s.so` is present in your toolchain.

### **8. Update Package Dependencies**

Ensure that your package dependencies are accurate.

**Modify the `DEPENDS` variable in your `Makefile`:**

```makefile
define Package/helloworld
  SECTION:=utils
  CATEGORY:=Utilities
  TITLE:=Helloworld -- prints a snarky message
  DEPENDS:=+libstdcpp +libpthread +librt +libgcc
endef
```

Note: Use `+libgcc` instead of `+libgcc_s` because OpenWrt packages typically refer to `libgcc`.

### **9. Review Compiler and Linker Output**

Enable verbose output to get detailed information about the compilation and linking process.

**Compile with verbose flags:**

```bash
make package/helloworld/compile V=99
```

Examine the output to ensure that:

- The correct compiler and linker flags are being used.
- The libraries are being linked in the correct order.
- No unexpected flags are disabling exceptions or affecting linking.

### **10. Check for CMake Overrides**

Ensure that CMake isn't introducing flags that conflict with your settings.

- **Review `CMakeLists.txt` for flags:** Remove any settings that might disable exceptions or enforce static linking.
- **Explicitly Set CMake Variables:**

  ```cmake
  set(CMAKE_CXX_FLAGS "${TARGET_CXXFLAGS}")
  set(CMAKE_EXE_LINKER_FLAGS "${TARGET_LDFLAGS}")
  ```

### **11. Try Linking with `-lgcc_eh`**

In some cases, linking against `libgcc_eh` can resolve `_Unwind_Resume` references.

**Update `TARGET_LDFLAGS`:**

```makefile
TARGET_LDFLAGS += -lstdc++ -lgcc_eh -lm
```

### **12. Double-Check for Any Static Libraries**

Ensure that no static libraries are being linked inadvertently.

- **Avoid Static Libraries:** Ensure all linked libraries are shared versions.
- **Check Build Logs:** Look for any `*.a` files being linked instead of `*.so`.

### **Summary of Your `Makefile` and `CMakeLists.txt`**

**`Makefile`:**

```makefile
include $(TOPDIR)/rules.mk

PKG_NAME:=helloworld
PKG_VERSION:=1.0
PKG_RELEASE:=1

include $(INCLUDE_DIR)/package.mk
include $(INCLUDE_DIR)/cmake.mk

define Package/helloworld
  SECTION:=utils
  CATEGORY:=Utilities
  TITLE:=Helloworld -- prints a snarky message
  DEPENDS:=+libstdcpp +libpthread +librt +libgcc
endef

# Enable exceptions by removing -fno-exceptions
TARGET_CXXFLAGS += -fno-rtti

TARGET_LDFLAGS += -lstdc++ -lgcc -lm

CMAKE_OPTIONS += \
    -DCMAKE_BUILD_TYPE=Release

define Package/helloworld/description
  Simple helloworld program for OpenWrt.
endef

define Build/Prepare
	mkdir -p $(PKG_BUILD_DIR)
	$(CP) ./src/* $(PKG_BUILD_DIR)/
endef

define Package/helloworld/install
	$(INSTALL_DIR) $(1)/bin
	$(INSTALL_BIN) $(PKG_BUILD_DIR)/helloworld $(1)/bin/
endef

$(eval $(call BuildPackage,$(PKG_NAME)))
```

**`src/CMakeLists.txt`:**

```cmake
cmake_minimum_required(VERSION 3.0)
project(helloworld CXX)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(helloworld helloworld.cpp)

# Link against standard libraries
target_link_libraries(helloworld
    stdc++
    gcc
    m
    pthread
    rt
)

# Ensure proper compiler and linker flags are applied
set_target_properties(helloworld PROPERTIES
    COMPILE_FLAGS "${CMAKE_CXX_FLAGS}"
    LINK_FLAGS "${CMAKE_EXE_LINKER_FLAGS}"
)
```

### **Additional Tips**

- **Check for Macros or Definitions:** Ensure no macros are disabling exceptions (e.g., `-DNO_EXCEPTIONS`).
- **Consistency Across Code:** All code compiled within your package should have consistent compiler flags.
- **Verify OpenWrt SDK Components:** Ensure that all OpenWrt SDK components are up-to-date and not corrupted.

### **Why the Issue Occurs**

The `_Unwind_Resume` function is part of GCC's low-level exception handling mechanism. When exceptions are disabled using `-fno-exceptions`, the compiler doesn't generate the necessary unwinding code in your objects, but the standard library may still reference these functions. This mismatch leads to undefined references during linking.

### **References from Your Research**

- Mixing compilers or different versions can cause ABI mismatches.
- Exception handling models (e.g., DWARF-2 vs. SJLJ) must be consistent across all code and libraries.
- Static linking of standard libraries can introduce symbol resolution issues.
- Other developers have resolved similar issues by ensuring compiler flags and library versions are consistent.

### **Conclusion**

By enabling exceptions and ensuring consistent compiler and linker settings, you should be able to resolve the undefined reference to `_Unwind_Resume`. Remember that even if your code doesn't use exceptions, the standard libraries might, so it's essential to compile with exceptions enabled unless you're certain that all code (including libraries) is built without them.

Feel free to ask if you have any questions or need further assistance!