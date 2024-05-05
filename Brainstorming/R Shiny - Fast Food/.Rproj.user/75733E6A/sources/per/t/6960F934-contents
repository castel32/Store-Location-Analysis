# Resturants
rest = read.csv("/Users/c32/Documents/NYCDSA/Projects/2 R Data Analysis/Fast-Food/Data/Fast Food America/Datafiniti_Fast_Food_Restaurants_Jun19.csv", header = TRUE)

# Let's try some automated EDA

#dataMaid
install.packages('dataMaid')
library(dataMaid)
makeDataReport(rest, output='html', replace = TRUE)

#DataExplorer
install.packages('DataExplorer')
library(DataExplorer)
create_report(rest)
data()

# SmartEDA
install.packages("SmartEDA")
# Import library
library(SmartEDA)
ExpReport(rest,op_file='smartEDA.html')

# Census

