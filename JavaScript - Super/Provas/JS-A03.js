// [JS-A03] Você foi contratado(a) para desenvolver um programa que irá auxiliar um professor a calcular algumas estatísticas das notas 
// de seus alunos. O programa deve solicitar ao professor o número total de estudantes na turma e, em seguida, pedir que ele insira as 
// notas de cada aluno individualmente. Após receber todas as notas, o programa deverá calcular a média da turma e identificar a maior 
// e a menor nota obtida.

// Instruções:

// Solicite ao professor que digite o número total de estudantes na turma.
// Em seguida, peça que o professor insira a nota de cada aluno individualmente, uma por vez.
// Calcule a média da turma somando todas as notas e dividindo pelo número total de estudantes.
// Identifique e registre a maior nota obtida na turma.
// Ao final, exiba a média da turma e a maior e a menor nota encontrada.

// Dicas:

// Utilize um loop while para coletar as notas de todos os alunos.
// Armazene as notas em uma variável e vá atualizando o valor da soma a cada nova nota inserida.
// Compare cada nota com a maior nota atualmente registrada para encontrar a maior nota.
// Para calcular a média, divida a soma das notas pelo número total de estudantes.
// Exiba os resultados de forma clara e organizada.


// Lembre-se de testar o programa com diferentes valores de notas e número de estudantes para garantir que ele funcione corretamente
//  em diversas situações. Boa programação!

// Obs: executar como node js-A03.js


const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

// Cabeçalho 
console.log("===========================================");
console.log("       Cálculo de Estatísticas das Notas  ");
console.log("===========================================");
console.log("Este programa calcula a média da turma, a maior nota e a menor nota ");
console.log("a partir das notas inseridas pelo professor para cada aluno.");
console.log("===========================================");

function calcularEstatisticas(totalStudents) {
  let studentNotes = [];
  let maxNote = 0;
  let minNote = Infinity;
  let totalNotes = 0;
  let currentStudent = 1;

  // Loop while para coletar as notas dos alunos
  const loopNotas = () => {
    rl.question(`Digite a nota do aluno ${currentStudent}: `, (note) => {
      const parsedNote = parseFloat(note);

      if (isNaN(parsedNote) || parsedNote < 0 || parsedNote > 100) {
        console.log('A nota deve ser um número entre 0 e 100.');
        loopNotas(); 
      } else {
        studentNotes.push(parsedNote);
        totalNotes += parsedNote;
        maxNote = Math.max(maxNote, parsedNote);
        minNote = Math.min(minNote, parsedNote);

        currentStudent++;

        if (currentStudent <= totalStudents) {
          loopNotas(); 
        } else {
          calcularMediaEMostrarResultados();
        }
      }
    });
  };

  // Função que calcula a média e exibe os resultados
  function calcularMediaEMostrarResultados() {
    const averageNote = totalNotes / totalStudents;
    console.log("\n=== Resultados ===");
    console.log(`Média da turma: ${averageNote.toFixed(2)}`);
    console.log(`Maior nota: ${maxNote}`);
    console.log(`Menor nota: ${minNote}`);
    rl.close();
  }

  loopNotas(); // Inicia a coleta das notas
}

// Solicita o número total de estudantes
rl.question('Digite o número total de estudantes na turma: ', (numStudents) => {
  const totalStudents = parseInt(numStudents);
  if (isNaN(totalStudents) || totalStudents <= 0) {
    console.log('O número de estudantes deve ser um número inteiro positivo.');
    rl.close();
  } else {
    calcularEstatisticas(totalStudents);
  }
});

rl.on('close', () => {
  console.log('Programa encerrado.');
});
