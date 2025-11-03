import os

def generate_index():
    # Get all .ttl files from the rdf_players directory
    rdf_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'rdf_players')
    ttl_files = [f for f in os.listdir(rdf_dir) if f.endswith('.ttl')]
    
    # Sort filenames alphabetically
    ttl_files.sort()
    
    # Generate player links
    player_links = []
    for filename in ttl_files:
        player_name = os.path.splitext(filename)[0].replace('_', ' ')
        player_links.append(f'      <a href="rdf_players/{filename}" class="player-link">{player_name}</a>')
    
    # Create the HTML content
    html_content = """<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Football Players Data</title>
    <style>
      body {
        font-family: Arial, sans-serif;
        line-height: 1.6;
        max-width: 1200px;
        margin: 0 auto;
        padding: 20px;
      }
      h1 {
        text-align: center;
        color: #333;
      }
      .players-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
        gap: 10px;
        padding: 20px 0;
      }
      .player-link {
        display: block;
        padding: 8px 12px;
        color: #0066cc;
        text-decoration: none;
        border-radius: 4px;
        transition: background-color 0.2s;
      }
      .player-link:hover {
        background-color: #f0f0f0;
        text-decoration: underline;
      }
    </style>
  </head>
  <body>
    <h1>Football Players Data</h1>
    <div class="players-grid">
""" + '\n'.join(player_links) + """
    </div>
  </body>
</html>"""
    
    # Write to index.md
    with open('index.md', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"Generated index with {len(ttl_files)} players")

if __name__ == "__main__":
    generate_index()
