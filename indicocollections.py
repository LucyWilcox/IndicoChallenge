import indicoio
from indicoio.custom import Collection
import secret

indicoio.config.api_key = secret.api_key

collection2 = Collection("colleection_name")
collection4 = Collection("colleeeection_name")
# Add Data
# collection.add_data([["indico is so easy", "label1"], ["text2", "label2"]])
# collection2.add_data([["https://upload.wikimedia.org/wikipedia/commons/2/27/Hillary_Clinton_official_Secretary_of_State_portrait_crop.jpg", "hillary"], ["http://i2.cdn.turner.com/money/dam/assets/160224112545-trump-nevada-victory-speech-780x439.jpg", "trump"]])

# collection3.add_data([["https://images-na.ssl-images-amazon.com/images/I/515LuXdi5ZL._SY355_.jpg", "Monet", "Impressionism"], ["http://destinationwilliamstown.org/wp-content/uploads/2015/01/Monet_Outbound.jpg", "Monet", "Impressionism"],["https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/Claude_Monet_-_Meules,_milieu_du_jour.jpg/279px-Claude_Monet_-_Meules,_milieu_du_jour.jpg", "Monet", "Impressionism"], ["https://www.ibiblio.org/wm/paint/auth/monet/first/impression/impression.jpg", "Monet", "Impressionism"], ["http://www.kepeslap.com/images/22848/ren.jpg", "Renior", "Impressionism"], ["https://s-media-cache-ak0.pinimg.com/736x/5e/09/40/5e0940c7c67179aa515b4052ebe43d59.jpg", "Renior"], ["http://www.restaurant-renoir.de/upload/sonstige_bilder/galerie4g.jpg", "Renior", "Impressionism"], ["http://fr.wahooart.com/A55A04/w.nsf/O/BRUE-8EWPLG/$File/PIERRE-AUGUSTE-RENOIR-ALGIERS-THE-GARDEN-OF-ESSAI.JPG", "Renior", "Impressionism"]] )
collection4.add_data([["https://images-na.ssl-images-amazon.com/images/I/515LuXdi5ZL._SY355_.jpg", "Impressionism"], ["http://destinationwilliamstown.org/wp-content/uploads/2015/01/Monet_Outbound.jpg", "Impressionism"],["https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/Claude_Monet_-_Meules,_milieu_du_jour.jpg/279px-Claude_Monet_-_Meules,_milieu_du_jour.jpg", "Impressionism"], ["https://www.ibiblio.org/wm/paint/auth/monet/first/impression/impression.jpg", "Impressionism"], ["http://www.kepeslap.com/images/22848/ren.jpg", "Impressionism"], ["https://s-media-cache-ak0.pinimg.com/736x/5e/09/40/5e0940c7c67179aa515b4052ebe43d59.jpg", "Impressionism"], ["http://www.restaurant-renoir.de/upload/sonstige_bilder/galerie4g.jpg", "Impressionism"], ["http://fr.wahooart.com/A55A04/w.nsf/O/BRUE-8EWPLG/$File/PIERRE-AUGUSTE-RENOIR-ALGIERS-THE-GARDEN-OF-ESSAI.JPG", "Impressionism"]] )

collection4.add_data([["http://www.metmuseum.org/toah/images/h5/h5_1999.363.35.jpg", "Cubism"], ["https://upload.wikimedia.org/wikipedia/en/archive/8/82/20150118143030!Albert_Gleizes,_l'Homme_au_Balcon,_1912,_oil_on_canvas,_195.6_x_114.9_cm,_Philadelphia_Museum_of_Art.jpg", "Cubism"], ["http://robinurton.com/history/20th%20c/cubism/Picasso/ReservoirHorta9.jpg", "Cubism"] ])
# Training
collection4.train()

# Telling Collection to block until ready
collection4.wait()

# Done! Start analyzing text
print collection4.predict("http://images.easyart.com/i/prints/lg/4/5/45126.jpg")
print collection4.predict("https://s-media-cache-ak0.pinimg.com/236x/19/30/f2/1930f26bbe50c5014384d9a39bc1ec32.jpg")
print collection4.predict("http://cdn.pursuitist.com/wp-content/uploads/2014/10/cubism1-800x660.jpg")
# print collection3.predict("http://www.restaurant-renoir.de/upload/sonstige_bilder/galerie4g.jpg")