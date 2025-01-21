# /tmp/openwrt-sdk/openwrt-sdk-23.05.3-ath79-generic_gcc-12.3.0_musl.Linux-x86_64/feeds/packages/lang/golang/golang/Makefile

The error message you're encountering:

```
Makefile:422: *** missing separator (did you mean TAB instead of 8 spaces?).  Stop.
```

indicates a syntax issue in your `Makefile` at line **422**. In GNU Make, such an error typically arises when there is incorrect indentation—specifically, when a line that should **not** be indented is indented, or when commands that should be indented with a **TAB character** are instead indented with spaces.

Let's analyze your `Makefile` to identify and resolve the issue.

## Analyzing the Makefile

From the output you've provided, line **422** is:

```makefile
$(eval $(call HostBuild))
```

This line is supposed to invoke the `HostBuild` process and should **not** be indented.

Let's look at the surrounding lines in your `Makefile`:

```makefile
define Package/golang-src/extra_provides
	echo 'libc.so.6'
endef

$(eval $(call HostBuild))
$(eval $(call BuildPackage,golang))
$(eval $(call BuildPackage,golang-doc))
$(eval $(call BuildPackage,golang-src))
```

**Issues Identified:**

1. **Indented `endef`:**

   The `endef` after the `define Package/golang-src/extra_provides` block may be incorrectly indented. In GNU Make, both `define` and `endef` must start at the **beginning of the line** with **no indentation**. If `endef` is indented with spaces or tabs, it will cause a parsing error.

2. **Incorrect Indentation Before `$(eval ...)` Lines:**

   Similarly, the lines starting with `$(eval $(call ...))` should **not** be indented. They must start at the very beginning of the line.

3. **Commands Within `define` Block:**

   The `echo 'libc.so.6'` line inside the `define` block should be indented with a **TAB character**, not spaces.

## Steps to Resolve the Error

### 1. Ensure `endef` Is Not Indented

Check the indentation of the `endef` keyword after your `define Package/golang-src/extra_provides` block. It should have **no spaces or tabs** before it.

#### Incorrect (Indented `endef`):

```makefile
endef
```

*(If this line is indented with spaces or tabs, it is incorrect.)*

#### Correct (No Indentation):

```makefile
endef
```

### 2. Ensure `$(eval ...)` Lines Are Not Indented

Make sure that the lines invoking `$(eval ...)` are not indented. They should start at the beginning of the line.

#### Incorrect (Indented Lines):

```makefile
    $(eval $(call HostBuild))
    $(eval $(call BuildPackage,golang))
    $(eval $(call BuildPackage,golang-doc))
    $(eval $(call BuildPackage,golang-src))
```

*(If these lines are indented with spaces or tabs, they are incorrect.)*

#### Correct (No Indentation):

```makefile
$(eval $(call HostBuild))
$(eval $(call BuildPackage,golang))
$(eval $(call BuildPackage,golang-doc))
$(eval $(call BuildPackage,golang-src))
```

### 3. Ensure Proper Indentation with Tabs for Commands

Commands within a `define` or a rule must be indented with a **TAB character**.

In your `define Package/golang-src/extra_provides` block:

#### Incorrect (Indented with Spaces):

```makefile
define Package/golang-src/extra_provides
    echo 'libc.so.6'
endef
```

*(The `echo` command is indented with spaces.)*

#### Correct (Indented with a TAB):

```makefile
define Package/golang-src/extra_provides
	echo 'libc.so.6'
endef
```

*(The `echo` command is indented with a TAB character.)*

### 4. Check for Other Indentation Issues

Use your text editor to display whitespace characters, ensuring that:

- All commands within rules or `define` blocks are indented with **TAB characters**.
- Keywords like `define` and `endef`, and variable assignments are **not indented**.
- There are no extraneous spaces or tabs at the beginning of lines where they shouldn't be.

### 5. Verify the Makefile Syntax

After making the corrections, your `Makefile` should look like this:

```makefile
# ... [Previous content of your Makefile]

# src/debug contains ELF executables as test data
# and they reference these libraries
# we need to call this in Package/$(1)/extra_provides
# to pass CheckDependencies in include/package-ipkg.mk
define Package/golang-src/extra_provides
	echo 'libc.so.6'
endef

$(eval $(call HostBuild))
$(eval $(call BuildPackage,golang))
$(eval $(call BuildPackage,golang-doc))
$(eval $(call BuildPackage,golang-src))
```

**Notes:**

- **No Indentation on `endef` and `$(eval ...)` Lines:** Ensure there are no spaces or tabs before these lines.
- **Commands Indented with TAB:** The `echo 'libc.so.6'` line is indented with a TAB character.
- **Consistent Formatting:** Maintain consistent indentation and spacing throughout the Makefile.

## Verifying the Makefile

After making these changes, save the `Makefile` and attempt to build again:

```bash
make package/tollgate-module-relay-go/compile V=s
```

## Additional Tips

- **Configure Your Text Editor:**

  - Set your editor to display whitespace characters to easily identify spaces and tabs.
  - Configure your editor so that when editing Makefiles, pressing the Tab key inserts a **TAB character**, not spaces.

- **Check for Mixed Indentation:**

  - Mixing tabs and spaces can cause subtle errors. Ensure that you're consistently using tabs for indentation in Makefiles.

- **Use Diagnostic Tools:**

  - Use the `grep` command you've used previously to locate lines starting with spaces:

    ```bash
    grep -nP '^\s+[^ \t#]' Makefile
    ```

  - This can help you identify lines that may be incorrectly indented.

- **Clean the Build Directory:**

  - If you continue to experience issues, consider cleaning the build directory:

    ```bash
    make package/feeds/packages/golang/{clean,dirclean}
    ```

## Conclusion

The `missing separator` error is often caused by incorrect indentation in your `Makefile`. By ensuring that:

- `define` and `endef` keywords, as well as `$(eval ...)` lines, are **not indented**.
- Commands within `define` blocks or rules are indented with a **TAB character**.
- There are no extraneous spaces or tabs at the beginning of lines.

you should be able to resolve the error and successfully build your package.

---

If you need further assistance or encounter additional errors, feel free to provide the updated error messages and `Makefile` content, and I'll be happy to help!