app.config(function($translateProvider){
  console.log("QUI");
  $translateProvider
    .preferredLanguage($('html').attr('lang'))
    .fallbackLanguage('en')
    .useSanitizeValueStrategy(null)
    .translations('it', {
      TESTO: "Testo",
      TESTO_CON_VARIABILE: "Testo {{var}}"
    })
    .translations('en', {
      TESTO: "Text",
      TESTO_CON_VARIABILE: "Text {{var}}"
    })
  ;
});
