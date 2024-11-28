import configparser
import argparse
import pandas as pd
import html

def parse_mapping_file(filepath):
    """Parse the mapping file into a pandas DataFrame."""
    df = pd.read_csv(filepath, sep='\t', header=None, skiprows=1,  # Skip first row
                     names=['Category', 'SubCategory', 'Name', 'Mapping'])
    # Fill empty SubCategory with Category if needed
    df['SubCategory'] = df['SubCategory'].fillna('')
    return df

def format_button_combination(mapping):
    """
    Convert button combinations to PromptFont CSS classes.
    """
    # Expanded mapping of button names to PromptFont CSS classes
    button_classes = {
        'A': {'class': 'pf-xbox-a', 'color': 'pf-color-green'},
        'B': {'class': 'pf-xbox-b', 'color': 'pf-color-red'},
        'X': {'class': 'pf-xbox-x', 'color': 'pf-color-blue'},
        'Y': {'class': 'pf-xbox-y', 'color': 'pf-color-yellow'},
        'LB': {'class': 'pf-xbox-left-shoulder', 'color': 'pf-color-red-gradient'},
        'RB': {'class': 'pf-xbox-right-shoulder', 'color': 'pf-color-green-gradient'},
        'LT': {'class': 'pf-xbox-left-trigger', 'color': 'pf-color-red-gradient'},
        'RT': {'class': 'pf-xbox-right-trigger', 'color': 'pf-color-green-gradient'},
        'LS': {'class': 'pf-analog-l-click', 'color': 'pf-color-analog-l'},
        'RS': {'class': 'pf-analog-r-click', 'color': 'pf-color-analog-r'},
        'LS:X': {'class': 'pf-analog-l-left-right', 'color': 'pf-color-analog-l'},
        'LS:Y': {'class': 'pf-analog-l-up-down', 'color': 'pf-color-analog-l'},
        'LS:XY': {'class': 'pf-analog-l-any', 'color': 'pf-color-analog-l'},
        'RS:X': {'class': 'pf-analog-r-left-right', 'color': 'pf-color-analog-r'},
        'RS:Y': {'class': 'pf-analog-r-up-down', 'color': 'pf-color-analog-r'},
        'RS:XY': {'class': 'pf-analog-r-any', 'color': 'pf-color-analog-r'},
        'Start': {'class': 'pf-xbox-menu', 'color': 'pf-color-black'},
        'Back': {'class': 'pf-xbox-view', 'color': 'pf-color-black'},
        '▲': {'class': 'pf-dpad-up', 'color': 'pf-color-black'}, 
        '▼': {'class': 'pf-dpad-down', 'color': 'pf-color-black'}, 
        '▶': {'class': 'pf-dpad-right', 'color': 'pf-color-black'},
        '◀': {'class': 'pf-dpad-left', 'color': 'pf-color-black'},
        '▲▶': {'class': 'pf-gamepad-up-right', 'color': 'pf-color-black'}, 
        '▼▶': {'class': 'pf-dpad-right-down', 'color': 'pf-color-black'}, 
        '◀▼': {'class': 'pf-dpad-left-down', 'color': 'pf-color-black'}, 
        '◀▲': {'class': 'pf-dupad-left-up', 'color': 'pf-color-black'}, 
        'LP1': {'class': 'pf-gamepad-l4', 'color': 'pf-color-dark-purple'},
        'LP2': {'class': 'pf-gamepad-l5', 'color': 'pf-color-dark-purple'},
        'RP1': {'class': 'pf-gamepad-r4', 'color': 'pf-color-dark-brown'},
        'RP2': {'class': 'pf-gamepad-r5', 'color': 'pf-color-dark-brown'},
        '/': {'class': 'pf-device-x360', 'color': 'pf-color-black'}
    }
    
    # Custom button combo conversion
    mapping = mapping.replace(', ', '+')
    
    # Create spans with PromptFont classes and color styling
    def format_button(btn):
        button_info = button_classes.get(btn, {'class': 'pf-button-press', 'color': 'pf-color-black'})
        return f'<span class="pf {button_info["class"]} {button_info["color"]}"></span>'
    
    # Convert to PromptFont button icons
    return ''.join(format_button(btn) for btn in mapping.split('+'))

def generate_html_cheatsheet(df, column_size=3, font_size=7):
    """
    Generate an HTML cheat sheet with 3-column layout and consolidated categories.
    """
    # HTML template with enhanced styling
    html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Controller Mapping Cheat Sheet</title>
    <link rel="stylesheet" href="promptfont.css">
    <style>
        @page {{
            size: A4 auto;
            margin: 3mm;
        }}
        body {{
            font-family: メイリオ, Arial, sans-serif;
            font-size: {font_size}pt;
            line-height: 1;
            background-color: #ffffff;
        }}
        .container {{
            column-count: {column_size};
            column-gap: 3px;
        }}
        .category-section {{
            background-color: #ffffff;
            border: 1px solid #e0e0e0;
            margin-bottom: 3px;
            break-inside: avoid;
            padding: 2px;
            border-radius: 2px;
        }}
        .category-header {{
            font-weight: bold;
            background-color: #1c1c1c;
            color: white;
            padding: 2px;
            text-align: left;
            margin-bottom: 2px;
        }}
        table {{
            width: 100%;
            table-layout: fixed;
            border-collapse: collapse;
            margin-bottom: 2px;
        }}
        td {{
            padding: 0px 1px;
            border: 1px solid #d0d0d0;
            overflow: hidden;
            text-overflow: ellipsis;
            white-space: nowrap;
        }}
        td:nth-child(1) {{
            font-size: {font_size-2}pt;
            text-align: right;
            padding-right: 3px;
        }}
        td:nth-child(2) {{
            font-size: {font_size}pt;
            text-align: left;
            padding-left: 2px;
        }}
        .pf {{
            font-size: {font_size}pt;
            margin: 0 1px;
        }}
        
        /* Custom color gradients */
        .pf-color-green {{ 
            background: linear-gradient(to bottom right, #00FF00, #000000);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        .pf-color-red {{ 
            background: linear-gradient(to bottom right, #FF0000, #000000);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        .pf-color-blue {{ 
            background: linear-gradient(to bottom right, #3333FF, #000000);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        .pf-color-yellow {{ 
            background: linear-gradient(to bottom right, #FFAA00, #000000);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        .pf-color-black {{ color: black; }}
        .pf-color-red-gradient {{
            background: linear-gradient(to bottom, #FF0000, #000000);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        .pf-color-green-gradient {{
            background: linear-gradient(to bottom, #00FF00, #000000);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        .pf-color-analog-l {{
            background: radial-gradient(#FF0000, #000000, #000000);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        .pf-color-analog-r {{
            background: radial-gradient(#00FF00, #000000, #000000);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        .pf-color-dark-purple {{
            background: linear-gradient(to right, #4B0082, #000000);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        .pf-color-dark-brown {{
            background: linear-gradient(to right, #5D4037, #000000);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
    </style>
</head>
<body>
    <div class="container">
"""
    
    # Preserve the original order of categories from the input file
    category_order = df['Category'].unique()
    
    # Iterate through original category order
    for category in category_order:
        # Filter dataframe for this category
        group = df[df['Category'] == category]
        
        # Group by SubCategory within the main category to preserve hierarchy
        subgrouped = group.groupby('SubCategory')
        
        html_content += f'<div class="category-section">\n'
        html_content += f'<div class="category-header">{html.escape(category)}</div>\n'
        html_content += """
    <table>
      <colgroup>
        <col style="width:68%;">
        <col style="width:32%;">
      </colgroup>
"""
        
        # Add rows for each subcategory group
        for subcategory, subgroup in subgrouped:
            # Add subcategory as a header row if it exists and is different from category
            if subcategory and subcategory != category:
                html_content += f'<tr><td colspan="2" style="background-color:#88aadd;color:#FFFFFF;font-weight:bold;text-align:center;">{html.escape(subcategory)}</td></tr>\n'
            
            # Add mapping rows
            for _, row in subgroup.iterrows():
                html_content += f'<tr><td>{html.escape(row["Name"])}</td><td>{format_button_combination(row["Mapping"])}</td></tr>\n'
        
        html_content += '</table>\n'
        html_content += '</div>\n'
    
    html_content += """
    </div>
</body>
</html>
"""
    return html_content

def main():
    config = configparser.ConfigParser()
    config.read('config.ini', 'UTF-8')

    parser = argparse.ArgumentParser(description='convert controller mapping tsv to cheatsheet')

    parser.add_argument('-i', '--input_file', help='source file path or url (Default:set from config.ini)')
    parser.add_argument('-o', '--output_file', default='controller_mapping_cheatsheet.html', help='output html file path (Default:controller_mapping_cheatsheet.html)')
    parser.add_argument('-c', '--column_size', type=int, default=3, choices=[1, 2, 3, 4], help='number of columns (Defualt:3)')
    parser.add_argument('-fs', '--font_size', type=float, default=12, help='fontsize (Defualt:12)')

    args = parser.parse_args()

    if args.input_file:
        input_file = args.input_file
    else:
        input_file = config['PATH']['input_file']

    # Write output to a file
    with open(args.output_file, 'w', encoding='utf-8') as f:

        df = parse_mapping_file(input_file)
        html_output = generate_html_cheatsheet(df, args.column_size, args.font_size)  # Reduced font size to maximize content
        f.write(html_output)
    
    print("Cheat sheet HTML generated successfully!")

if __name__ == '__main__':
    main()
