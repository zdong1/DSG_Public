library("leaflet")
library("tidyverse")
library("htmltools")
library("data.table")
train_df <- fread("training_CONFIDENTIAL.csv", showProgress=FALSE)
train_df[, 
         list(label=HTML(paste(sep="<br>",paste("Bedrooms:", BedroomCnt),
                               paste("Bathrooms:", BathroomCnt),
                               paste("Total area:", FinishedSquareFeet),
                               paste("Sales Price: $", SaleDollarCnt)))), 
       list(Longitude, Latitude)] %>% leaflet() %>% addTiles() %>%addCircleMarkers(
         lat =  ~ Latitude / 1e6,
         lng =  ~ Longitude / 1e6,
         label = ~label,
         clusterOptions = markerClusterOptions()
         )

train_df$CountyID<- as.numeric(train_df$ZoneCodeCounty)

# Make an interactive query table for different built years
train_df[, list(n=.N, Mean.Price=mean(SaleDollarCnt), SD.Price=sd(SaleDollarCnt)), 
         by=BuiltYear] %>%round(3) %>% datatable()
