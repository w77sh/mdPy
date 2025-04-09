import markdown
import pyfiglet
import argparse
from rich.console import Console
from rich.panel import Panel

console = Console()

def show_welcome_screen():
    ascii_art = pyfiglet.figlet_format("md to html")
    console.print(f"[bold cyan]{ascii_art}[/bold cyan]")
   
    console.print(Panel("[bold green]Welcome to Markdown to HTML Converter![/bold green]\n\n"
                        
                "[bold cyan]Convert your Markdown files to HTML effortlessly.[/bold cyan]\n\n"

                "[bold ]Usage:[/bold]\n"
                "  - Provide the input Markdown file path.\n"
                "  - Specify the output HTML file path.\n",
             title="md to html ", subtitle="Welcome to the Converter", border_style="bold blue"))

def md_to_html(input, output):
        
        with open(input, 'r', encoding='utf-8') as md_file,open(output, 'w', encoding='utf-8') as html_file:
            html_file.write(markdown.markdown(md_file.read()))
        console.print(Panel(f"[green]✅ Successfully converted![/green]\n📄 ,[bold]Output:[/bold] {output}", title="md to html", border_style=""))


if __name__ == "__main__":
    show_welcome_screen()
    
    parser = argparse.ArgumentParser(description="📄 Markdown to HTML Converter")
    parser.add_argument('-i', '--input', required=True, help='Path to md file')
    parser.add_argument('-o', '--output', required=True, help='Path to html file')
    args = parser.parse_args()
    
    md_to_html(args.input, args.output)