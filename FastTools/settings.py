from rich.console import Console

console = Console()

welcome_message = 'Welcome To FastTools v1'

class Start:
  def __init__(
    self,
    YouTube = False,
    Discord = False
  ):
    self.YouTube = YouTube
    self.Discord = Discord
    #Run Welcome Message
    Start.welcome(self)
  
  def welcome(self):
    console.print(welcome_message, style="Red Bold Italic")

    all_features = [
      ["YouTube",self.YouTube],
      ["Discord",self.Discord]
      ]

    enabled_features = []

    for x in all_features:
      if x[1]:
        enabled_features.append(x[0])
    
    if len(enabled_features):
      enabled_features = ",".join(enabled_features)
      enabled_features = f"Enabled Features: {enabled_features}"
    else:
      enabled_features = 'There is no features enabled currently!'
    
    console.print(enabled_features, style="#F4B52E bold")
      
    
  
  

  