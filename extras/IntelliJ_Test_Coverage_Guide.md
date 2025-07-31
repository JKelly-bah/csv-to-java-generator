# Test Coverage in IntelliJ IDEA Ultimate - Complete Guide

## Table of Contents
1. [How to Use Test Coverage in IntelliJ Ultimate](#1-how-to-use-test-coverage-in-intellij-ultimate)
2. [Coverage Display Options](#2-coverage-display-options)
   - 2a. [Switching from Gutter to Line Highlighting and Customizing Coverage Colors](#2a-switching-from-gutter-to-line-highlighting-and-customizing-coverage-colors)
   - 2b. [Understanding Coverage Menu Options](#2b-understanding-coverage-menu-options)

---

## 1. How to Use Test Coverage in IntelliJ Ultimate

### Step 1: Enable Coverage Collection
1. Right-click on your test class or test method in the Project Explorer
2. Select **"Run '[TestName]' with Coverage"** from the context menu
   
   > **Screenshot Placeholder**: Add screenshot showing the right-click context menu with "Run with Coverage" option highlighted

3. Alternatively, you can:
   - Use the keyboard shortcut: `Ctrl+Shift+F10` (Windows/Linux) or `Cmd+Shift+R` (macOS) while having a test selected
   - Click the **Run with Coverage** button in the toolbar (green arrow with a shield icon)
   
   > **Screenshot Placeholder**: Add screenshot of the toolbar showing the "Run with Coverage" button

### Step 2: View Coverage Results
1. After running tests with coverage, the **Coverage** tool window will automatically open on the right of the screen
2. You'll see a tree view showing:
   - **Packages** and their coverage percentages
   - **Classes** and their coverage percentages
   - **Methods** and their coverage percentages

   > **Screenshot Placeholder**: Add screenshot of the Coverage tool window showing the coverage tree with percentages

### Step 3: Interpret Coverage Information
- **Green highlighting**: Lines that were executed during tests
- **Red highlighting**: Lines that were NOT executed during tests
- **Yellow highlighting**: Lines that were partially executed (for branches/conditions)

---


## 2. Coverage Display Options

### 2a. Switching from Gutter to Line Highlighting and Customizing Coverage Colors

By default, IntelliJ shows coverage as colored squares in the gutter (left margin). You can change this to full line highlighting and customize the colors:

#### Step 1: Access Coverage Settings
1. Go to **File** → **Settings** (Windows/Linux) or **IntelliJ IDEA** → **Preferences** (macOS)
2. Navigate to **Build, Execution, Deployment** → **Coverage**

   > **Screenshot Placeholder**: Add screenshot of the Settings/Preferences window with the Coverage section highlighted in the left panel

#### Step 2: Customize Coverage Colors and Display
1. In Settings/Preferences, go to **Editor** → **Color Scheme** → **General**
2. Expand the **Line Coverage** section
3. Here you can customize colors for:
   - **Full**: Lines that are completely covered by tests
   - **Partial**: Lines that are partially covered (like branches where only some conditions were tested)
   - **Uncovered**: Lines that were not executed by any tests

   > **Screenshot Placeholder**: Add screenshot showing the Line Coverage color customization options in the Color Scheme settings

#### Step 3: Access Coverage Controls in the Editor
When coverage is active, you'll see coverage control options directly in the editor:
1. To access these options, left-click on the gutter highlight (colored indicator) next to the test-covered code.
2. This will open a popup showing:
   - **"Hide coverage"**: Temporarily hide coverage highlighting (shown immediately in the popup)
   - **Settings gear icon**: Click to open the "Edit Coverage Colors" dialog for quick access to color customization
   - **Hit count information**: Displays how many times the line was executed

> **Screenshot Placeholder**: Add screenshot showing the coverage popup after clicking the gutter highlight, with the Hide coverage option and settings gear icon visible

#### Step 4: Configure Coverage Display Options
To access the main Coverage settings page:
1. Go to **File** → **Settings** (Windows/Linux) or **IntelliJ IDEA** → **Preferences** (macOS).
2. Navigate to **Build, Execution, Deployment** → **Coverage** in the left sidebar.

In the main Coverage settings page, you'll find several important options:

##### When new coverage is gathered:
- **Show options before applying coverage to the editor** (default): Prompts you each time
- **Do not apply collected coverage**: Coverage data is collected but not displayed
- **Replace active suites with the new one**: Automatically replaces existing coverage
- **Add to the active suites**: Combines with existing coverage data

##### Coverage Display Settings:
- **Activate Coverage View**: ✅ (Checked by default) - Shows the Coverage tool window
- **Show coverage in the project view**: ✅ (Checked by default) - Displays coverage percentages in the Project Explorer

   > **Screenshot Placeholder**: Add screenshot of the Coverage settings page showing these options as they appear in the interface

#### Step 5: Java Coverage Specific Settings

##### Coverage Runner:
- **Choose coverage runner**: Set to "IntelliJ IDEA" (default) or other runners like JaCoCo

##### Coverage Options:
- **Branch coverage**: ✅ Collect coverage for all branches of if/switch statements
- **Track per test coverage**: Collect data about which code lines were covered by specific tests
- **Collect coverage in test folders**: Include test code itself in coverage analysis
- **Ignore implicitly declared default constructors**: ✅ (Recommended) - Excludes auto-generated constructors

##### Exclude annotations:
- Add annotations here to exclude classes/methods from coverage (e.g., `*Generated*`)

   > **Screenshot Placeholder**: Add screenshot showing the Java Coverage section with all these options visible

#### Visual Comparison:
- **Gutter highlighting**: Small colored squares in the left margin
- **Line highlighting**: Entire lines are highlighted with background colors

> **Screenshot Placeholder**: Add side-by-side comparison showing the same code with gutter highlighting vs. line highlighting

> **Note**: The specific option to switch between gutter and line highlighting may be found in the editor appearance settings or may be controlled through the coverage view options in the Coverage tool window itself.

### 2b. Understanding Coverage Menu Options

#### Accessing the Coverage Menu
After running tests with coverage, you can access coverage-related options in several ways:

##### Method 1: Click on Coverage Gutter Indicators (Most Direct)
1. **Left-click on any coverage indicator** (colored dot/square) in the gutter (left margin)
2. This will show a popup with:
   - **"Hit count information"** (e.g., "Hits: 5")
   - **"Hide coverage"** button to temporarily hide coverage highlighting
   - **Settings gear icon** (⚙️) that opens the Coverage color scheme settings
3. Click the **settings gear icon** to access the Line Coverage color customization

   > **Screenshot Placeholder**: Add screenshot showing the popup that appears when clicking on a coverage gutter indicator, highlighting the hit count, hide coverage button, and settings gear

##### Method 2: Main Menu Access (Most Reliable)
1. Go to **Run** → **Show Coverage Data** in the main menu bar
2. Or go to **Run** → **Coverage** for additional coverage options

   > **Screenshot Placeholder**: Add screenshot of the Run menu showing coverage-related options

##### Method 3: Coverage Tool Window Menu
1. After running tests with coverage, the **Coverage tool window** appears to the right of IntelliJ
2. Right-click on any item in the coverage tree (packages, classes, or methods)
3. Access coverage options from this context menu

   > **Screenshot Placeholder**: Add screenshot of the Coverage tool window with right-click context menu visible

##### Method 4: In-Editor Coverage Controls
When coverage is active, you may see coverage control options directly in the editor:
1. Look for small icons/controls that appear when coverage highlighting is active
2. Options like **"Hide coverage"** and **"Edit Coverage Colors"** may appear

   > **Screenshot Placeholder**: Add screenshot showing any additional coverage controls that appear in the editor when coverage is active

##### Method 5: Right-click in Source Code Editor (Sometimes Available)
1. Open any **source code file** (.java, .kt, .scala, etc.) that has coverage data
2. Right-click anywhere **in the code editor area** (not in the gutter or line numbers)
3. Look for the **Coverage** submenu in the context menu

   > **Screenshot Placeholder**: Add screenshot of the right-click context menu in a source code file with Coverage submenu highlighted

> **Important Notes:**
> - Clicking on coverage gutter indicators is the most direct way to access coverage information and controls
> - The settings gear icon in the gutter popup provides quick access to color customization
> - The Coverage submenu in the editor context menu **may not always appear**, even when coverage highlighting is active
> - The most reliable way to access comprehensive coverage options is through the **Run** menu in the main menu bar

#### Coverage Menu Options Explained:

##### **"Show Coverage Data"**
- **Purpose**: Opens the Coverage Data dialog to manage multiple coverage files
- **Use case**: When you have multiple test runs or want to combine coverage from different sources

##### **"Generate Coverage Report"**
- **Purpose**: Creates an HTML coverage report
- **Options available**:
  - **Output directory**: Where to save the report
  - **Open in browser**: Automatically open the report after generation
  
  > **Screenshot Placeholder**: Add screenshot of the Generate Coverage Report dialog

##### **"Export Coverage Data"**
- **Purpose**: Export coverage data to various formats (XML, CSV, etc.)
- **Use case**: For integration with other tools or reporting systems

##### **"Coverage Settings"**
- **Purpose**: Quick access to coverage-related settings
- **Redirects to**: The Coverage section in Settings/Preferences
- **Tip for Line Highlighting**: To enable line highlighting for coverage, deselect the "Foreground" option and select the "Background" option for the coverage color. This will highlight the entire line instead of just the text. If both options are selected, the text may become very difficult to read due to overlapping color effects.

##### **"Hide Coverage"**
- **Purpose**: Temporarily hide coverage highlighting without losing the data
- **Note**: Coverage data remains loaded, just not displayed

##### **"Switch Coverage Suite"**
- **Purpose**: Switch between different loaded coverage datasets
- **Use case**: When you have multiple coverage files loaded and want to compare

   > **Screenshot Placeholder**: Add screenshot showing the dropdown list when multiple coverage suites are available

#### Coverage Tool Window Options

In the Coverage tool window (bottom panel), you'll find additional options:

##### Toolbar Buttons:
- **🔄 Refresh**: Reload coverage data
- **📊 Generate Report**: Create HTML coverage report
- **⚙️ Coverage Settings**: Open coverage preferences
- **❌ Close**: Close the coverage tool window

   > **Screenshot Placeholder**: Add screenshot of the Coverage tool window toolbar with buttons labeled

##### Coverage Tree Context Menu:
Right-click on any item in the coverage tree for options like:
- **"Jump to Source"**: Navigate to the selected class/method
- **"Exclude from Coverage"**: Remove specific packages/classes from coverage analysis

   > **Screenshot Placeholder**: Add screenshot of the coverage tree context menu

#### Additional Coverage Features:

##### **Branch Coverage**
- Shows coverage for conditional statements (if/else, switch cases)
- Displayed as yellow highlighting for partially covered branches

##### **Coverage Annotations**
- Hover over coverage indicators to see detailed statistics
- Shows: Lines covered, Lines total, Percentage

   > **Screenshot Placeholder**: Add screenshot of a coverage tooltip showing detailed statistics

---

## Tips and Best Practices

### 1. Performance Considerations
- Large projects may experience slower performance with coverage enabled
- Consider running coverage on specific test suites rather than all tests

### 2. Coverage Thresholds
- Set up coverage thresholds in your build tool to enforce minimum coverage requirements
- IntelliJ will respect these thresholds when displaying results

### 3. Excluding Files from Coverage
- Use the Coverage settings to exclude generated files, test utilities, or third-party code
- This provides more accurate coverage metrics for your actual business logic

---

## Troubleshooting

### Common Issues:

#### "No coverage data available"
- **Solution**: Ensure tests were run with coverage enabled
- **Check**: Verify that JaCoCo is properly configured in your build file

#### "Coverage highlighting not showing"
- **Solution**: Check that coverage highlighting is enabled in settings
- **Verify**: Coverage data is loaded in the Coverage Data dialog



---

*This guide covers IntelliJ IDEA Ultimate version 2023.3 and later. Some menu locations and options may vary in different versions.*

---

h2. Screenshot Summary

Below is a summary list of all screenshot placeholders mentioned throughout this guide. Replace each placeholder with the actual screenshot as needed:

# Right-click context menu with "Run with Coverage" option highlighted
# Toolbar showing the "Run with Coverage" button
# Coverage tool window showing the coverage tree with percentages
# Settings/Preferences window with the Coverage section highlighted in the left panel
# Line Coverage color customization options in the Color Scheme settings
# Coverage popup after clicking the gutter highlight, with the Hide coverage option and settings gear icon visible
# Coverage settings page showing coverage options as they appear in the interface
# Java Coverage section with all options visible
# Side-by-side comparison showing the same code with gutter highlighting vs. line highlighting
# Popup that appears when clicking on a coverage gutter indicator, highlighting the hit count, hide coverage button, and settings gear
# Run menu showing coverage-related options
# Coverage tool window with right-click context menu visible
# Additional coverage controls that appear in the editor when coverage is active
# Right-click context menu in a source code file with Coverage submenu highlighted
# Generate Coverage Report dialog
# Dropdown list when multiple coverage suites are available
# Coverage tool window toolbar with buttons labeled
# Coverage tree context menu
# Coverage tooltip showing detailed statistics




Shade Name	    Hex Code	        Use Case Suggestion
Soft Red	            #803333		    Subtle, not too distracting - works, more burgundy
Warm Red	        #CC4444		Balanced, noticeable but not harsh - works
~~True Red	    #FF5555		    Attention-grabbing, readable~~ washes out text
Bright Red	        #FF4444		Slightly brighter, good for warnings
Intense Red	    #FF0000		    Strong signal, use sparingly - too bright??
~~Neon Red	    #FF4C4C		Very vibrant, useful for critical hits~~ washes out text




Shade Name	    Hex Code	        Use Case Suggestion
Soft Green	        #335C33		 Subtle, barely draws attention
Bright Green	    #00FF00	         Very bright, signals "success" strongly - bright but works
Neon Green	    #39FF14	         Eye-catching, high contrast - bright but works

Shade Name	    Hex Code	        Use Case Suggestion
Soft Yellow	        #7A6200	    Low distraction, earthy tone - works
Bright Yellow	    #FFFF00		    Bold, may need dark outline to stand out - works but bright
Neon Yellow	    #FFFF33		    Very bright, should be used sparingly - works, pale bright