'use strict';

const functions = require('firebase-functions'),
      admin = require('firebase-admin'),
      logging = require('@google-cloud/logging')();

admin.initializeApp(functions.config().firebase);

exports.createBirthCertificate = functions.database.ref('/data/{id}/data').onWrite(event => {
  const my_data = event.data.val();
  
  if (my_data === null) return null;
  admin.database().ref(`/data/${event.params.id}/birth_certificate`).once('value')
    .then(snapshot => {
      var val = snapshot.val();
      
      admin.database().ref(`/data/${event.params.id}/birth_certificate/ckid`).set(event.params.id);
      if (my_data.lat) {
        if (!val || !val.lat) admin.database().ref(`/data/${event.params.id}/birth_certificate/lat`).set(my_data.lat);
      }
      if (my_data.lng) {
        if (!val || !val.lng) admin.database().ref(`/data/${event.params.id}/birth_certificate/lng`).set(my_data.lng);
      }
      
    });
  
  // RAMO birth_certificate
  // birthID: IDENTIFICATIVO DATI DI ORIGINE (LI HO TROVATI SUL LIBRO XY PAG 11)
  // ckid: IL NOME DEL NODO
  // lat: LA LATITUDINE DELL'OGGETTO (o il centroide dello shape)
  // lon: LA LOGITUDINE DELL'OGGETTO (o il centroide dello shape)
  // recorder: MAIL DELL'UTENTE CHE STA REGISTRANO (O ID UTENTE SU FIREBASE)
  // type: NOME DEL GRUPPO INIZIALE DELLA REGISTRAZIONE
  // dob: DATE OF BIRTH
  // dor: DATE OF REGISTRATION
  // parentID: (OPZIONALE) elemento padre (campana del campanile XY)
  // shape: (OPZIONALE) LO SHAPE {:coordinates => (on array di lat e lng), :type => 'Polygon'}
  
  // RAMO DATA 
  // CAMPI CHIAVE/VALORE IN BASE AL "FORM" DEL GRUPPO
  
  // RAMO MEDIA 
  // ELENCO ID DI IMMAGINI/AUDIO ECC
  
  return true;
});
