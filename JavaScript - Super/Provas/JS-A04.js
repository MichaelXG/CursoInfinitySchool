// [JS-A04] Você é um desenvolvedor de software que trabalha em uma equipe especializada em criar ferramentas matemáticas para uma empresa 
// do mercado financeiro. A empresa precisa de uma nova funcionalidade para sua plataforma online, permitindo que os usuários obtenham 
// informações sobre cálculos matemáticos importantes relacionados aos investimentos.

// Sua tarefa é criar um módulo JavaScript que ofereça aos usuários a possibilidade de inserir um número inteiro positivo e, em resposta,
// calcular o fatorial desse número e também a sequência de Fibonacci até aquele número. Isso ajudará os investidores a realizar análises
// mais detalhadas sobre suas decisões financeiras.

// Obs: executar como node js-A04.js

// Cabeçalho
console.log("=================================================");
console.log("       Ferramenta de Cálculos Matemáticos        ");
console.log("=================================================");
console.log("Este programa permite que você insira um número  ");
console.log("inteiro positivo e, em resposta, calcula:        ");
console.log("- O fatorial do número fornecido                 ");
console.log("- A sequência de Fibonacci até o número fornecido");
console.log("=================================================\n");

// Importa o módulo readline para entrada do usuário
const readline = require('readline');

// Módulo de Cálculos Matemáticos
const MathModule = (() => {
  // Função para calcular o fatorial de um número
  const fatorial = (n) => {
    if (n < 0) return null; // Verificação de número negativo
    if (n === 0 || n === 1) return 1;
    let resultado = 1;
    for (let i = 2; i <= n; i++) {
      resultado *= i;
    }
    return resultado;
  };

  // Função para calcular a sequência de Fibonacci até um número
  const fibonacci = (n) => {
    if (n < 0) return null; // Verificação de número negativo
    const sequencia = [0, 1];
    for (let i = 2; i <= n; i++) {
      sequencia.push(sequencia[i - 1] + sequencia[i - 2]);
    }
    return sequencia.slice(0, n + 1);
  };

  // Função principal que recebe um número e retorna o fatorial e a sequência de Fibonacci
  const calcular = (numero) => {
    if (numero < 0 || !Number.isInteger(numero)) {
      return "Por favor, insira um número inteiro positivo.";
    }
    return {
      fatorial: fatorial(numero),
      fibonacci: fibonacci(numero)
    };
  };

  return { calcular };
})();

// Configura o readline para capturar entrada do usuário
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

// Pergunta ao usuário para inserir um número
rl.question('Digite um número inteiro positivo: ', (input) => {
  const numero = parseInt(input);

  // Calcula e exibe os resultados
  const resultado = MathModule.calcular(numero);
  if (typeof resultado === 'string') {
    console.log(resultado);
  } else {
    console.log(`Fatorial de ${numero}:`, resultado.fatorial);
    console.log(`Sequência de Fibonacci até ${numero}:`, resultado.fibonacci);
  }

  // Fecha o readline
  rl.close();
});
