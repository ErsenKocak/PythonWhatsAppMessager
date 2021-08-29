import Services.MessageService as messageService
import Services.FileService as fileService

userData = fileService.readCsvFile()
def main():
  print()
  
main()
messageService.sendMessage(userData)