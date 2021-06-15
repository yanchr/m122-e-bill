import ftpKundensystemService
import parse

ftpKundensystemService.grabFile()
parsedText = parse.parse_csv()
parse.parse_to_txt(parsedText)

