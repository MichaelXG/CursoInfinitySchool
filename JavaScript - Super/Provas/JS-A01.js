// [JS-A01] Considere três notas (n1, n2, n3) e seus respectivos pesos (p1, p2, p3). 
// Calcule a média ponderada das notas e atribua o resultado à variável "media". Após o cálculo, exiba a média ponderada no console.
// OBS: Para calcular a média ponderada multiplica os valores das notas pelos valores dos pesos, e divide pelas somas de todos os pesos. 
// Lembre-se de declarar valores para os pesos e para as notas.

    function calcularMediaPonderada(n1, n2, n3, p1, p2, p3) {
        let media = (n1 * p1 + n2 * p2 + n3 * p3) / (p1 + p2 + p3);
        media = Math.round(media * 100) / 100; 
        return media;
    }
  
    let nota1 = 8;
    let nota2 = 7;
    let nota3 = 9;
    
    let peso1 = 0.25;
    let peso2 = 0.35;
    let peso3 = 0.40;

    let media = calcularMediaPonderada(nota1, nota2, nota3, peso1, peso2, peso3);
    console.log("Média ponderada: " + media);