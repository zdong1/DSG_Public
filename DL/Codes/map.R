# This is initially an interative map/table I wrote for Zillow Challenges
# For confidentiality reasons, key variables have been removed (V1, DV1, CV1, etc. are all variables)
# Zhihang Dong
library("leaflet")
library("tidyverse")
library("htmltools")
library("data.table")
# Using Leaflet to do interactive mapping
train_df <- fread("yourdata.csv", showProgress=FALSE)
train_df[, 
         list(label=HTML(paste(sep="<br>",paste("v1:", v1),
                               paste("v2:", v2),
                               paste("v3:", v3),
                               paste("v4: $", v4)))), 
       list(Longitude, Latitude)] %>% leaflet() %>% addTiles() %>%addCircleMarkers(
         lat =  ~ Latitude / 1e6,
         lng =  ~ Longitude / 1e6,
         label = ~label,
         clusterOptions = markerClusterOptions()
         )

train_df$someID<- as.numeric(train_df$somecode)

# Make an interactive query table for different built years
train_df[, list(n=.N, Mean.Price=mean(DV1), SD.Price=sd(DV1)), 
         by=CV1] %>%round(3) %>% datatable()
