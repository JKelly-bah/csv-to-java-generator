# IntelliJ IDEA Ultimate: Complete Test Coverage Guide

## Table of Contents
1. [Using Test Coverage in IntelliJ Ultimate](#1-using-test-coverage-in-intellij-ultimate)
2. [Adding JaCoCo.exec File for Test Coverage](#2-adding-jacocoexec-file-for-test-coverage)
3. [Coverage Display Options](#3-coverage-display-options)
   - 3a. [Changing Gutter Highlight to Line Highlighting](#3a-changing-gutter-highlight-to-line-highlighting)
   - 3b. [Understanding Coverage Menu Options](#3b-understanding-coverage-menu-options)

---

## 1. Using Test Coverage in IntelliJ Ultimate

### Step 1: Enable Test Coverage
1. Open your project in IntelliJ IDEA Ultimate
2. Navigate to the **Menu Bar** at the top of the IntelliJ window and click on **Run**
3. From the **Run** dropdown menu, select **Run with Coverage**
   - Alternatively, look for the coverage icon (shield with checkmark) in the **main toolbar** and click it

**[Screenshot Placeholder: Main IntelliJ interface showing the Run menu with "Run with Coverage" option highlighted]**

### Step 2: Run Tests with Coverage
1. Right-click on your test class, test method, or test package
2. Select **"Run [TestName] with Coverage"** from the context menu
3. Alternatively, use the keyboard shortcut: `Ctrl+Shift+F10` (Windows/Linux) or `Cmd+Shift+R` (macOS)

**[Screenshot Placeholder: Context menu showing "Run with Coverage" option when right-clicking on a test file]**

### Step 3: View Coverage Results
After running tests with coverage, you'll see:
- Coverage percentage in the **Coverage** tool window
- Color-coded lines in your source files:
  - **Green**: Covered lines
  - **Red**: Uncovered lines
  - **Yellow**: Partially covered lines (e.g., branches)

> **Note:** By default, IntelliJ displays coverage indicators in the **gutter** (the narrow column on the left side of the code editor). If you prefer full **line highlighting** instead of or in addition to gutter indicators, see [Section 3a: Changing Gutter Highlight to Line Highlighting](#3a-changing-gutter-highlight-to-line-highlighting) for detailed configuration instructions.

**[Screenshot Placeholder: Code editor showing green and red highlighted lines indicating coverage status]**

**[Screenshot Placeholder: Coverage tool window at the bottom showing coverage statistics and percentages]**

---

## 2. Adding JaCoCo.exec File for Test Coverage

### Step 1: Locate Your JaCoCo.exec File
1. Find your `jacoco.exec` file (typically located in `target/jacoco.exec` for Maven projects or `build/jacoco/test.exec` for Gradle projects)
2. Note the full path to this file

**[Screenshot Placeholder: File explorer showing the location of jacoco.exec file in project structure]**

### Step 2: Import JaCoCo Coverage Data
1. Navigate to the **Menu Bar** at the top of the IntelliJ window and click on **Run**
2. From the **Run** dropdown menu, select **Show Coverage Data**
3. In the **Coverage Data Management** dialog that opens, click the **"+"** button (plus sign) in the top-left area of the dialog
4. From the dropdown that appears, select **"Import from file"**
5. In the file browser dialog, navigate to your `jacoco.exec` file and select it
6. Click **"OK"** to import the file

**[Screenshot Placeholder: Coverage Data Management dialog with the "+" button highlighted and import options visible]**

**[Screenshot Placeholder: File browser dialog for selecting the jacoco.exec file]**

### Step 3: Configure Coverage Suite
1. In the **Coverage Data Management** dialog, you can:
   - Name your coverage suite
   - Set the coverage runner to **JaCoCo**
   - Specify include/exclude patterns for packages or classes
2. Click **"OK"** to apply the coverage data

**[Screenshot Placeholder: Coverage suite configuration dialog showing JaCoCo settings and include/exclude patterns]**

### Step 4: View Imported Coverage
1. The coverage data will now be displayed in your editor
2. Check the **Coverage** tool window for detailed statistics
3. You can switch between different coverage suites using the dropdown in the Coverage tool window

**[Screenshot Placeholder: Coverage tool window showing imported JaCoCo data with multiple coverage suites in dropdown]**

---

## 3. Coverage Display Options

### 3a. Changing Gutter Highlight to Line Highlighting

#### Step 1: Access Coverage Display Settings
1. Navigate to the **Menu Bar** at the top of the IntelliJ window
2. Click on **File** (Windows/Linux) or **IntelliJ IDEA** (macOS)
3. From the dropdown menu, select **Settings** (Windows/Linux) or **Preferences** (macOS)
4. In the **Settings/Preferences** dialog that opens, look at the **left panel** with the tree structure
5. Navigate to **Editor** → **General** → **Code Coverage** by:
   - Clicking the **Editor** folder to expand it
   - Clicking the **General** subfolder to expand it
   - Clicking on **Code Coverage**

**[Screenshot Placeholder: Settings/Preferences dialog with Editor > General > Code Coverage section highlighted in the left panel]**

#### Step 2: Configure Coverage Highlighting
In the Code Coverage settings, you'll find:

1. **"Show coverage in gutter"** - Controls gutter indicators
2. **"Highlight lines"** - Controls line highlighting
3. **"Use covered lines color"** - Enables/disables color coding

**Configuration Options:**
- **Gutter Only**: Check "Show coverage in gutter", uncheck "Highlight lines"
- **Line Highlighting**: Check "Highlight lines", optionally uncheck "Show coverage in gutter"
- **Both**: Check both options for maximum visibility

**[Screenshot Placeholder: Code Coverage settings panel showing checkboxes for "Show coverage in gutter" and "Highlight lines" options]**

#### Step 3: Customize Colors (Optional)
1. In the same **Code Coverage** settings panel, look for and click the **"Colors"** link/button
2. This will navigate you to **Editor** → **Color Scheme** → **General** → **Code Coverage** in the settings tree
3. In this section, you can customize colors for:
   - **Covered lines/branches**
   - **Uncovered lines/branches**
   - **Partially covered lines/branches**
4. Click on each color box to open the **color picker** and select your preferred colors

**[Screenshot Placeholder: Color scheme settings showing coverage color options with color pickers for different coverage states]**

### 3b. Understanding Coverage Menu Options

#### Accessing Coverage Options
**Method 1: Via Menu Bar**
1. Navigate to the **Menu Bar** at the top of the IntelliJ window and click on **Run**
2. From the **Run** dropdown menu, select **Coverage Options**

**Method 2: Via Coverage Tool Window**
1. Look for the **Coverage** tool window (usually at the bottom of the IDE)
2. In the **Coverage** tool window toolbar, click the **gear/settings icon** (⚙️)

**[Screenshot Placeholder: Run menu showing Coverage Options highlighted]**

**[Screenshot Placeholder: Coverage tool window with gear/settings icon highlighted]**

#### Coverage Menu Options Explained

**1. Coverage Runner**
- **IntelliJ IDEA**: Built-in coverage runner
- **JaCoCo**: External JaCoCo library
- **Emma**: Legacy coverage tool (less commonly used)

*Choose JaCoCo for better accuracy and industry-standard reporting*

**[Screenshot Placeholder: Coverage runner dropdown showing IntelliJ IDEA, JaCoCo, and Emma options]**

**2. Sampling Mode**
- **Tracing**: More accurate, slower execution
- **Sampling**: Faster execution, less precise

*Use Tracing for development, Sampling for large test suites*

**3. Enable Coverage in Test Folders**
- When checked: Includes test source files in coverage calculation
- When unchecked: Only measures production code coverage

*Typically unchecked to focus on production code coverage*

**4. Include/Exclude Patterns**
- **Include patterns**: Specify which packages/classes to include (e.g., `com.yourcompany.*`)
- **Exclude patterns**: Specify what to exclude (e.g., `*.test.*`, `*Test`, generated code)

*Use patterns to focus coverage on relevant code and exclude test utilities*

**[Screenshot Placeholder: Include/Exclude patterns dialog showing text fields with example patterns]**

**5. Branch Coverage**
- When enabled: Shows coverage for conditional branches (if/else, switch statements)
- When disabled: Only shows line coverage

*Enable for comprehensive coverage analysis*

**6. Coverage Data File**
- Specifies where coverage data is stored
- Can be customized for specific reporting needs

**[Screenshot Placeholder: Full coverage options dialog showing all the settings mentioned above]**

#### Additional Coverage Tool Window Features

**Coverage Tree View:**
- **Package View**: Shows coverage by package hierarchy
- **Class View**: Shows coverage by individual classes
- **Method View**: Shows coverage by methods

**[Screenshot Placeholder: Coverage tool window showing tree view with package/class/method hierarchy and coverage percentages]**

**Coverage Actions:**
- **Generate Coverage Report**: Creates HTML/XML reports
- **Export Coverage Data**: Saves coverage data for external analysis
- **Import Coverage Data**: Loads previously saved coverage data

**[Screenshot Placeholder: Coverage tool window toolbar showing Generate Report, Export, and Import buttons]**

---

## Tips and Best Practices

### Performance Optimization
- Use **Sampling mode** for large codebases
- Configure **exclude patterns** to skip irrelevant code
- Limit coverage scope to specific modules when working on large projects

### Coverage Goals
- **Line Coverage**: Aim for 80%+ on critical code paths
- **Branch Coverage**: Aim for 70%+ to ensure decision logic is tested
- Focus on **meaningful coverage** rather than just high percentages

### Troubleshooting
- If coverage isn't showing, verify the correct **Coverage Runner** is selected
- Check **include/exclude patterns** if certain classes aren't appearing
- Ensure tests are actually running by checking the **Run** tool window

**[Screenshot Placeholder: Run tool window showing test execution results with passed/failed indicators]**

---

## Screenshot Summary
This guide requires the following screenshots to be fully effective:

1. Main IntelliJ interface with Run menu
2. Context menu showing "Run with Coverage"
3. Code editor with coverage highlighting
4. Coverage tool window with statistics
5. File explorer showing jacoco.exec location
6. Coverage Data Management dialog
7. Coverage suite configuration
8. Settings/Preferences Code Coverage panel
9. Color scheme coverage settings
10. Coverage options dialog
11. Coverage tool window features
12. Run tool window with test results

*Add these screenshots in the corresponding placeholder locations for a complete visual guide.*
