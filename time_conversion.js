// La idea de esta funcion es que convierta, la hora dada en formato de 12 horas am/pm,
// convertirla a formato de 24 horas

// el aproach basicamente es este:
// si te dan:
// 12am, lo conviertes a 00
// 1am a 12pm, no haces nada
// 1pm a 12 pm, le sumas 12 horas.
// en todos los casos le quitas el am o pm, ya que eso no existe en el formato militar

function timeConversion(s) {
  let amPm = s.chartAt(8);
  let militaryHour = '';
  if (amPm == 'A') {
    if (s.substring(0, 2) == '12') {
      militaryHour == '00';
    }
  } else {
    militaryHpur = s.substring(0, 2);
  }
}
