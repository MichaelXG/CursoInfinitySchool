"use strict";

const today = new Date();
var monthSelected = today.getMonth(); // Mês corrente
let schedules = {}; // Armazena os agendamentos

const dateFormatOptions = {
  default: { weekday: "long" },
  short: { day: "2-digit", month: "2-digit", year: "numeric" },
};

const formatDate = (day, month, year, locale = "pt-BR") => {
  // Ajuste no mês (em JavaScript, os meses são baseados em 0, então subtrai 1)
  const date = new Date(year, month - 1, day);
  return new Intl.DateTimeFormat(locale, {
    day: "2-digit",
    month: "2-digit",
    year: "numeric",
  }).format(date);
};

//----------------------------------------
const countries = [
  { code: "BR", flag: "flag-icon-br", name: "Brazil", locale: "pt-BR" },
  { code: "US", flag: "flag-icon-us", name: "USA", locale: "en-US" },
  { code: "FR", flag: "flag-icon-fr", name: "France", locale: "fr-FR" },
  { code: "DE", flag: "flag-icon-de", name: "Germany", locale: "de-DE" },
  { code: "ES", flag: "flag-icon-es", name: "Spain", locale: "es-ES" },
  { code: "IT", flag: "flag-icon-it", name: "Italy", locale: "it-IT" },
  { code: "JP", flag: "flag-icon-jp", name: "Japan", locale: "ja-JP" },
  { code: "CN", flag: "flag-icon-cn", name: "China", locale: "zh-CN" },
  { code: "IN", flag: "flag-icon-in", name: "India", locale: "hi-IN" },
  { code: "RU", flag: "flag-icon-ru", name: "Russia", locale: "ru-RU" },
  { code: "CA", flag: "flag-icon-ca", name: "Canada", locale: "en-CA" },
  { code: "AU", flag: "flag-icon-au", name: "Australia", locale: "en-AU" },
  {
    code: "GB",
    flag: "flag-icon-gb",
    name: "United Kingdom",
    locale: "en-GB",
  },
  { code: "MX", flag: "flag-icon-mx", name: "Mexico", locale: "es-MX" },
  { code: "AR", flag: "flag-icon-ar", name: "Argentina", locale: "es-AR" },
  { code: "CO", flag: "flag-icon-co", name: "Colombia", locale: "es-CO" },
  { code: "CL", flag: "flag-icon-cl", name: "Chile", locale: "es-CL" },
  { code: "PT", flag: "flag-icon-pt", name: "Portugal", locale: "pt-PT" },
  { code: "KR", flag: "flag-icon-kr", name: "South Korea", locale: "ko-KR" },
  { code: "ZA", flag: "flag-icon-za", name: "South Africa", locale: "en-ZA" },
  {
    code: "AE",
    flag: "flag-icon-ae",
    name: "United Arab Emirates",
    locale: "ar-AE",
  },
  { code: "EG", flag: "flag-icon-eg", name: "Egypt", locale: "ar-EG" },
  { code: "NG", flag: "flag-icon-ng", name: "Nigeria", locale: "en-NG" },
  { code: "SE", flag: "flag-icon-se", name: "Sweden", locale: "sv-SE" },
  { code: "NO", flag: "flag-icon-no", name: "Norway", locale: "no-NO" },
  { code: "FI", flag: "flag-icon-fi", name: "Finland", locale: "fi-FI" },
  { code: "DK", flag: "flag-icon-dk", name: "Denmark", locale: "da-DK" },
  { code: "NL", flag: "flag-icon-nl", name: "Netherlands", locale: "nl-NL" },
  { code: "BE", flag: "flag-icon-be", name: "Belgium", locale: "fr-BE" },
  { code: "CH", flag: "flag-icon-ch", name: "Switzerland", locale: "de-CH" },
  { code: "IE", flag: "flag-icon-ie", name: "Ireland", locale: "en-IE" },
  { code: "IL", flag: "flag-icon-il", name: "Israel", locale: "he-IL" },
  { code: "PL", flag: "flag-icon-pl", name: "Poland", locale: "pl-PL" },
  { code: "AT", flag: "flag-icon-at", name: "Austria", locale: "de-AT" },
  { code: "HU", flag: "flag-icon-hu", name: "Hungary", locale: "hu-HU" },
  { code: "SG", flag: "flag-icon-sg", name: "Singapore", locale: "en-SG" },
  { code: "MY", flag: "flag-icon-my", name: "Malaysia", locale: "ms-MY" },
  { code: "TH", flag: "flag-icon-th", name: "Thailand", locale: "th-TH" },
  { code: "PH", flag: "flag-icon-ph", name: "Philippines", locale: "en-PH" },
  { code: "VN", flag: "flag-icon-vn", name: "Vietnam", locale: "vi-VN" },
  { code: "PK", flag: "flag-icon-pk", name: "Pakistan", locale: "ur-PK" },
  { code: "BD", flag: "flag-icon-bd", name: "Bangladesh", locale: "bn-BD" },
  { code: "UA", flag: "flag-icon-ua", name: "Ukraine", locale: "uk-UA" },
  { code: "RO", flag: "flag-icon-ro", name: "Romania", locale: "ro-RO" },
  { code: "GR", flag: "flag-icon-gr", name: "Greece", locale: "el-GR" },
  { code: "TR", flag: "flag-icon-tr", name: "Turkey", locale: "tr-TR" },
  { code: "LT", flag: "flag-icon-lt", name: "Lithuania", locale: "lt-LT" },
  { code: "LV", flag: "flag-icon-lv", name: "Latvia", locale: "lv-LV" },
  { code: "EE", flag: "flag-icon-ee", name: "Estonia", locale: "et-EE" },
];

function getCountryCodeFromLocale(locale) {
  // Verifica se o locale está no formato "língua-PAÍS"
  if (locale.includes("-")) {
    return locale.split("-")[1].toUpperCase(); // Retorna o código do país em maiúsculas
  }

  return "BR"; // Valor padrão para Brasil se o locale não tiver um código de país
}
//----------------------------------------

async function loadHolidays(locale = "pt-BR", month, year) {
  // Extrai o código do país a partir do locale
  const countryCode = getCountryCodeFromLocale(locale);

  // Obtém o ano e mês correntes se não forem fornecidos
  const today = new Date();
  const selectedYear = year !== undefined ? year : today.getFullYear();
  const selectedMonth = month !== undefined ? month : today.getMonth();

  // Função auxiliar para formatar datas
  const formatDate = (day, month, year) => {
    const date = new Date(year, month, day);
    return new Intl.DateTimeFormat(locale, {
      day: "2-digit",
      month: "2-digit",
      year: "numeric",
    }).format(date);
  };

  const holidays = await fetchHolidays(selectedYear, countryCode);

  // Filtra os feriados do mês atual
  const filteredHolidays = Object.keys(holidays)
    .filter((date) => {
      const [holidayYear, holidayMonth] = date.split("-").map(Number);
      return holidayMonth - 1 === selectedMonth && holidayYear === selectedYear;
    })
    .map((date) => {
      const [holidayYear, holidayMonth, holidayDay] = date
        .split("-")
        .map(Number);
      const formattedDate = formatDate(
        holidayDay,
        holidayMonth - 1,
        holidayYear
      );
      return `${formattedDate}: ${holidays[date]}`;
    })
    .join("<br>"); // Usando <br> para separar feriados

  const holidaysContainer = document.querySelector(".current-events ul");
  holidaysContainer.innerHTML = filteredHolidays;
}

async function getHolidays(locale = "pt-BR", month, year) {
  // Extrai o código do país a partir do locale
  const countryCode = getCountryCodeFromLocale(locale);

  // Obtém o ano e mês correntes se não forem fornecidos
  const today = new Date();
  const selectedYear = year !== undefined ? year : today.getFullYear();
  const selectedMonth = month !== undefined ? month : today.getMonth();

  // Função auxiliar para formatar datas
  const formatDay = (day, month, year) => {
    const date = new Date(year, month, day);
    return new Intl.DateTimeFormat(locale, {
      day: "2-digit",
    }).format(date);
  };

  try {
    const holidays = await fetchHolidays(selectedYear, countryCode);

    // Filtra os feriados do mês atual
    const filteredHolidays = Object.keys(holidays)
      .filter((date) => {
        const [holidayYear, holidayMonth] = date.split("-").map(Number);
        return (
          holidayMonth - 1 === selectedMonth && holidayYear === selectedYear
        );
      })
      .map((date) => {
        const [holidayYear, holidayMonth, holidayDay] = date
          .split("-")
          .map(Number);
        const formattedDay = formatDay(
          holidayDay,
          holidayMonth - 1,
          holidayYear
        );
        return formattedDay;
      });

    // console.log("Filtered Holidays:", filteredHolidays);

    return filteredHolidays; // Retorna os dias formatados
  } catch (error) {
    console.error("Erro ao carregar feriados:", error);
    return [];
  }
}

async function fetchHolidays(year, countryCode) {
  const url = `https://date.nager.at/Api/v2/PublicHolidays/${year}/${countryCode}`;
  try {
    const response = await fetch(url);
    const data = await response.json();

    // console.log("API Response:", data);

    const holidays = {};
    data.forEach((holiday) => {
      const date = holiday.date;
      holidays[date] = holiday.localName;
    });
    return holidays;
  } catch (error) {
    console.error("Error fetching holidays:", error);
    return {};
  }
}

function generateMonthAbbreviations(
  locale = "pt-BR",
  selectedMonth,
  selectedYear,
  countryCode
) {
  const today = new Date();
  const currentMonth = today.getMonth(); // Mês corrente
  const currentYear = today.getFullYear(); // Ano corrente

  // Usa o mês e ano selecionados, ou o corrente caso não sejam fornecidos
  const monthToUse = selectedMonth !== undefined ? selectedMonth : currentMonth;
  const yearToUse = selectedYear !== undefined ? selectedYear : currentYear;

  // Gera as abreviações dos meses
  const months = Array.from(
    { length: 12 },
    (_, i) =>
      new Date(yearToUse, i, 1)
        .toLocaleString(locale, { month: "short" })
        .replace(/^\w/, (c) => c.toUpperCase()) // Capitaliza a primeira letra
        .replace(/\.$/, "") // Remove o ponto final, se existir
  );

  // Seleciona o container dos meses
  const monthsContainer = document.querySelector("#calendar-months");

  // Cria o conteúdo para os meses abreviados, destacando o mês atual ou o selecionado
  const monthsHTML = months
    .map((month, index) => {
      const isCurrentOrSelectedMonth = index === monthToUse;
      const className = isCurrentOrSelectedMonth
        ? "month-cell month-color month-hover"
        : "month-cell month-hover";
      // Define o ID como 'monthSelected' para o mês selecionado e 'month' para os demais
      const id = isCurrentOrSelectedMonth ? "monthSelected" : "month";
      return `<th class="${className}" data-month="${index}" id="${id}">${month}</th>`;
    })
    .join("");

  // Adiciona a linha com as células dos meses no container
  monthsContainer.innerHTML = `<tr class="months month-row">${monthsHTML}</tr>`;

  // Adiciona o evento de clique para cada célula de mês
  document.querySelectorAll(".month-cell").forEach((cell) => {
    cell.addEventListener("click", function () {
      // Remove a cor de destaque do mês atual
      document
        .querySelectorAll(".month-cell")
        .forEach((c) => c.classList.remove("month-color"));

      // Adiciona a cor de destaque ao mês clicado
      this.classList.add("month-color");

      // Recupera o mês e o ano selecionados
      const selectedMonth = parseInt(this.getAttribute("data-month"), 10);
      const selectedYear =
        parseInt(document.getElementById("year").value, 10) || yearToUse;

      // Gera o calendário com o mês, ano e locale selecionados
      if (!isNaN(selectedMonth) && !isNaN(selectedYear)) {
        generateCalendar(locale, selectedMonth, selectedYear);
      }
    });
  });
}

function setupCalendar() {
  // Obtém o locale selecionado ou usa o padrão
  const locale = setupCountrySelector();
  const countryCode = getCountryCodeFromLocale(locale);

  // Obtém a data atual
  const today = new Date();
  const currentYear = today.getFullYear();
  const currentMonth = today.getMonth();

  // Obtém o elemento do ano selecionado e o mês selecionado
  const yearInput = document.getElementById("year");
  const monthInput = document.getElementById("month");

  // Define o ano e o mês selecionados
  let selectedYear = yearInput ? parseInt(yearInput.value, 10) : currentYear;
  let selectedMonth = monthInput
    ? parseInt(monthInput.value, 10) - 1
    : currentMonth;

  // Verifica se o mês selecionado é válido
  if (isNaN(selectedMonth) || selectedMonth < 0 || selectedMonth > 11) {
    selectedMonth = currentMonth;
    console.error(
      "Mês inválido selecionado. Usando mês corrente:",
      currentMonth + 1
    );
  }

  // Adiciona evento de clique para cada célula de mês
  document.querySelectorAll(".month-cell").forEach((monthCell, index) => {
    monthCell.addEventListener("click", () => {
      console.log("Mês clicado:", index);
      console.log("Ano selecionado:", selectedYear);

      // Gera o calendário com o locale, código do país, mês e ano selecionados
      generateCalendar(locale, index, selectedYear);

      // Atualiza o mês selecionado
      selectedMonth = index;
      if (monthInput) monthInput.value = selectedMonth + 1; // Atualiza o input do mês, assumindo que o input aceita 1-based month
    });
  });
}

function generateDaysOfWeek(locale = "pt-BR", year) {
  // Cria uma nova data para obter os dias da semana
  const daysOfWeek = Array.from({ length: 7 }, (_, i) => {
    const day = new Date(year, 0, i + 1); // Ajusta a data para começar corretamente no primeiro dia do ano
    const dayName = day
      .toLocaleDateString(locale, { weekday: "short" })
      .replace(/\.$/, ""); // Remove ponto final, se existir
    return { name: dayName, index: day.getDay() }; // Retorna o nome do dia e o índice (0 = domingo)
  });

  // Ordena os dias da semana pelo índice (0 = domingo, 1 = segunda, etc.)
  const orderedDaysOfWeek = daysOfWeek.sort((a, b) => a.index - b.index);

  // Selecione o elemento de cabeçalho do calendário
  const calendarHeader = document.querySelector("#calendar-header");

  if (calendarHeader) {
    // Cria o cabeçalho da tabela para os dias da semana ordenados
    calendarHeader.innerHTML = orderedDaysOfWeek
      .map((day) => `<th class="days">${day.name.toUpperCase()}</th>`)
      .join("");
  } else {
    console.warn("Elemento #calendar-header não encontrado.");
  }
}

async function generateCalendar(locale = "pt-BR", month, year) {
  const today = new Date();

  const currentMonth = month !== undefined ? month : today.getMonth();
  const currentYear = year !== undefined ? year : today.getFullYear();

  const holidays = await getHolidays(locale, currentMonth, currentYear);

  function isHoliday(day) {
    const formattedDay = day.toString().padStart(2, "0");
    return holidays.includes(formattedDay);
  }

  loadSchedulesFromLocalStorage();

  function isDayEvent(
    day,
    month = new Date().getMonth(),
    year = new Date().getFullYear()
  ) {
    const formattedDay = day.toString().padStart(2, "0");
    const formattedMonth = (month + 1).toString().padStart(2, "0");
    const formattedYear = year.toString();
    const formattedDate = `${formattedYear}-${formattedMonth}-${formattedDay}`;

    const events = schedules[""];

    console.log("events: ", events);

    if (events) {
      const eventsOnDate = events.filter(
        (event) => event.dateStart === formattedDate
      );
      return eventsOnDate.length; // Retorna o número de eventos
    } else {
      return 0;
    }
  }

  const firstDayOfMonth = new Date(currentYear, currentMonth, 1).getDay();
  const daysInMonth = new Date(currentYear, currentMonth + 1, 0).getDate();
  const lastDayOfPreviousMonth = new Date(
    currentYear,
    currentMonth,
    0
  ).getDate();

  generateMonthAbbreviations(locale, currentMonth, currentYear);
  generateDaysOfWeek(locale, currentYear);

  let calendarHTML = "";
  let date = 1;

  for (let i = 0; i < 6; i++) {
    calendarHTML += `<tr class="week-row week-${i + 1}">`;

    for (let j = 0; j < 7; j++) {
      if (i === 0 && j < firstDayOfMonth) {
        calendarHTML += `<td class="td-clear"><td class="grey">${String(
          lastDayOfPreviousMonth - firstDayOfMonth + j + 1
        ).padStart(2, "0")}</td> </td>`;
      } else if (date > daysInMonth) {
        const nextMonthDate = date - daysInMonth;
        calendarHTML += `<td class="td-clear"><td class="grey">${String(
          nextMonthDate
        ).padStart(2, "0")}</td></td>`;
        date++;
      } else {
        const isToday =
          date === today.getDate() &&
          currentMonth === today.getMonth() &&
          currentYear === today.getFullYear();
        const dayClass = isToday ? "circle active-day" : "";
        const numberOfEvents = isDayEvent(date, currentMonth, currentYear);
        const eventClass = isHoliday(date)
          ? "circle blue-light"
          : numberOfEvents > 0
          ? "circle orange clickable"
          : "";

        // Adiciona onclick apenas se houver eventos
        const onclickAttr =
          numberOfEvents > 0
            ? `onclick="handleDateClick('${currentYear}-${String(
                currentMonth + 1
              ).padStart(2, "0")}-${String(date).padStart(2, "0")}')"`
            : "";

        calendarHTML += `<td class="td-clear"><td class="${dayClass} ${eventClass}" ${onclickAttr} data-date="${currentYear}-${String(
          currentMonth + 1
        ).padStart(2, "0")}-${String(date).padStart(2, "0")}">${String(
          date
        ).padStart(2, "0")} ${
          numberOfEvents > 0
            ? `<span class="event-count">${numberOfEvents}</span>`
            : ""
        }</td> </td>`;
        date++;
      }
    }

    calendarHTML += "</tr>";
  }

  const calendarBody = document.querySelector("#calendar-body");
  if (calendarBody) {
    calendarBody.innerHTML = calendarHTML;
  }

  const numDateElement = document.querySelector(".num-date");
  const dayElement = document.querySelector(".day");

  if (numDateElement && dayElement) {
    numDateElement.textContent = today.toLocaleDateString(locale, {
      day: "2-digit",
    });
    dayElement.textContent = today
      .toLocaleDateString(locale, { weekday: "long" })
      .toUpperCase();
  }

  const yearElement = document.querySelector(".year");
  if (yearElement) {
    yearElement.textContent = currentYear;
  }

  if (typeof loadHolidays === "function") {
    loadHolidays(locale, currentMonth, currentYear);
  } else {
    console.warn("Função loadHolidays não está definida.");
  }

  attachEventListeners();
}

function displayCurrentDate(locale = "pt-BR") {
  // Extrai o código do país a partir do locale, se necessário
  const countryCode = getCountryCodeFromLocale(locale);

  const today = new Date();

  // Atualiza o dia (mantendo a lógica existente)
  const numDateElement = document.querySelector(".num-date");
  if (numDateElement) {
    numDateElement.textContent = today.toLocaleDateString(locale, {
      day: "2-digit",
    });
  }

  // Atualiza o ano (padrão ou selecionado)
  const yearElement = document.querySelector(".year");
  if (yearElement) {
    yearElement.textContent = today.getFullYear();
  }

  console.log(
    `Data exibida: ${today.toLocaleDateString(locale)} (${countryCode})`
  );
}

function displayCurrentMonthAndYear(locale = "pt-BR") {
  const today = new Date();

  // Extrai o código do país a partir do locale, se necessário
  const countryCode = getCountryCodeFromLocale(locale);

  // Configura as opções para formatação do mês e ano
  const options = { month: "long", year: "numeric" };
  const monthYearText = today.toLocaleDateString(locale, options).toUpperCase();

  // Atualiza o elemento com o texto do mês e ano
  const monthYearElement = document.querySelector("#calendar-months");
  if (monthYearElement) {
    monthYearElement.textContent = monthYearText;
  }

  console.log(`Mês e ano exibidos: ${monthYearText} (${countryCode})`);
}

function setupEventListeners() {
  const prevYearBtn = document.getElementById("prev-year");
  const nextYearBtn = document.getElementById("next-year");

  // Meses e ano atuais ou selecionados
  const yearElement = document.querySelector("#year");
  const monthElement = monthSelected;

  // Obtem o locale baseado na bandeira usando a função setupCountrySelector
  const locale = setupCountrySelector();

  // Mensagens de erro para elementos não encontrados
  if (!prevYearBtn) {
    console.error("Elemento 'prev-year' não encontrado no DOM.");
  }
  if (!nextYearBtn) {
    console.error("Elemento 'next-year' não encontrado no DOM.");
  }
  if (!yearElement) {
    console.error("Elemento '#year' não encontrado no DOM.");
  }
  if (!monthElement) {
    console.error("Elemento 'monthElement' não encontrado no DOM.");
  }

  // Verifica se todos os elementos necessários foram encontrados
  if (!prevYearBtn || !nextYearBtn || !yearElement || !monthElement) {
    console.error(
      "Um ou mais elementos necessários não foram encontrados no DOM. A execução será interrompida."
    );
    return; // Sai da função se não houver todos os elementos
  }

  // Função para manipular a mudança de ano
  const handleYearChange = (increment) => {
    const currentYear =
      parseInt(yearElement.textContent, 10) || new Date().getFullYear();
    const currentMonth = monthElement + 1; // Ajusta o mês para o formato 1-12

    const newYear = currentYear + increment;

    // Gera o calendário com os novos valores
    generateCalendar(locale, currentMonth - 1, newYear);

    // Atualiza o texto do elemento do ano
    yearElement.textContent = newYear;
  };

  // Adiciona eventos de clique nos botões de ano anterior e próximo
  prevYearBtn.addEventListener("click", () => handleYearChange(-1));
  nextYearBtn.addEventListener("click", () => handleYearChange(1));
}

function getLocaleFromFlag(flagIconClass) {
  // Extrai o código da bandeira da classe
  const flagCode = flagIconClass.replace("flag-icon-", "");

  // Busca o país correspondente no array
  const country = countries.find((c) => c.flag === `flag-icon-${flagCode}`);

  // Retorna o locale do país ou um valor padrão se não encontrado
  return country ? country.locale : "pt-BR";
}

function setupCountrySelector() {
  // Seleciona o elemento de seleção do país
  const selectSelectedElement = document.querySelector(".select-selected");

  if (!selectSelectedElement) {
    console.error("Elemento de seleção do país não encontrado.");
    return "pt-BR"; // Valor padrão se o elemento não for encontrado
  }

  // Seleciona o ícone da bandeira dentro do elemento
  const flagIconElement = selectSelectedElement.querySelector(".flag-icon");

  if (!flagIconElement) {
    console.error("Ícone da bandeira não encontrado.");
    return "pt-BR"; // Valor padrão se o ícone não for encontrado
  }

  // Obtém a classe do ícone da bandeira
  const flagIconClass = flagIconElement.className;
  // console.log("Classe do ícone da bandeira:", flagIconClass);

  // Obtém o locale com base na classe do ícone da bandeira
  const locale = getLocaleFromFlag(flagIconClass);
  // console.log("Locale correspondente:", locale);

  // Retorna o locale
  return locale;
}

function getSelectedMonth() {
  // Tenta encontrar o elemento que tem o ID 'monthSelected'
  const monthSelectedElement = document.getElementById("monthSelected");

  // Verifica se o elemento foi encontrado
  if (monthSelectedElement) {
    // Exibe o valor de "data-month"
    const selectedMonth = parseInt(
      monthSelectedElement.getAttribute("data-month"),
      10
    );
    console.log("Elemento com ID 'monthSelected' encontrado:", selectedMonth);
    return selectedMonth;
  }

  // Se não houver ID 'monthSelected', procura o elemento com a classe 'month-color'
  const monthColorElement = document.querySelector(".month-cell.month-color");

  // Verifica se o elemento foi encontrado
  if (monthColorElement) {
    // Exibe o valor de "data-month"
    const selectedMonth = parseInt(
      monthColorElement.getAttribute("data-month"),
      10
    );
    console.log(
      "Elemento com a classe 'month-color' encontrado:",
      selectedMonth
    );
    return selectedMonth;
  }

  // Se nenhum dos elementos for encontrado, exibe erro
  console.error(
    "Nenhum elemento com o ID 'monthSelected' ou classe 'month-color' foi encontrado."
  );
  return null;
}

// Função auxiliar para obter o locale a partir do countryCode
function getLocaleFromCountryCode(countryCode) {
  // Supondo que 'countries' seja um array de objetos contendo 'code' e 'locale'
  return (
    countries.find((country) => country.code === countryCode)?.locale || "pt-BR"
  );
}

document.addEventListener(
  "DOMContentLoaded",
  (locale = "pt-BR", month, year) => {
    const today = new Date();

    // Meses e ano atuais ou selecionados
    const currentMonth = month !== undefined ? month : today.getMonth();
    const currentYear = year !== undefined ? year : today.getFullYear();

    const customSelect = document.getElementById("custom-select");
    const selectSelected = customSelect.querySelector(".select-selected");
    const selectItems = customSelect.querySelector(".select-items");

    // Set default selected item to Brazil
    const defaultCountry = countries.find((country) => country.code === "BR");
    const defaultLocale = defaultCountry ? defaultCountry.locale : "pt-BR";

    // Add options to the custom select
    countries.forEach((country) => {
      const option = document.createElement("div");
      option.className = "select-item";
      option.innerHTML = `<span class="flag-icon ${country.flag}"></span> ${country.name}`;
      option.addEventListener("click", () => {
        selectSelected.innerHTML = `<span class="flag-icon ${country.flag}"></span> ${country.name}`;
        selectItems.style.display = "none";
        // Atualiza o locale e countryCode ao selecionar um país
        const countryCode = country.code;
        const locale = country.locale;
        generateCalendar(locale, currentMonth, currentYear);
      });
      selectItems.appendChild(option);
    });

    // Set default selection
    if (defaultCountry) {
      selectSelected.innerHTML = `<span class="flag-icon ${defaultCountry.flag}"></span> ${defaultCountry.name}`;
    }

    // Toggle dropdown on click
    selectSelected.addEventListener("click", () => {
      selectItems.style.display =
        selectItems.style.display === "block" ? "none" : "block";
    });

    // Close dropdown when clicking outside
    document.addEventListener("click", (event) => {
      if (!customSelect.contains(event.target)) {
        selectItems.style.display = "none";
      }
    });

    // clearSchedules();
    // Inicializa o calendário com o defaultLocale e defaultCountry
    setupCalendar();
    generateCalendar(defaultLocale);
    loadHolidays(defaultLocale);

    setupEventListeners();
  }
);
function saveSchedulesToLocalStorage() {
  // Converte o objeto schedules em uma string JSON formatada
  const formattedSchedules = JSON.stringify(schedules, null, 2); // O segundo parâmetro é o replacer e o terceiro é o número de espaços para indentação
  localStorage.setItem("events", formattedSchedules);
  console.log("Eventos salvos com sucesso!");
  // Recarrega a página
  location.reload();
}

function loadSchedulesFromLocalStorage() {
  const savedSchedules = localStorage.getItem("events");
  if (savedSchedules) {
    schedules = JSON.parse(savedSchedules);
    console.log("Eventos carregados com sucesso!");
    console.log("Eventos salvos:", schedules);
  } else {
    schedules = {};
    console.log("Nenhum evento encontrado. Inicializando como vazio.");
  }
}

function clearSchedules() {
  // Limpa o localStorage
  localStorage.removeItem("events");

  // Reinicia o objeto schedules
  schedules = {};

  console.log("Todos os eventos foram removidos com sucesso!");
  // Recarrega a página
  location.reload();
}

function attachEventListeners() {
  document.querySelectorAll(".circle.orange.clickable").forEach((day) => {
    day.addEventListener("dblclick", (e) => {
      const date = e.target.closest("td").dataset.date;
      loadSchedulesFromLocalStorage();

      // Verifica se existem eventos associados à data
      const events = schedules[date] || [];
      let scheduleIndex = null;

      // Percorre todos os elementos de eventos para encontrar o que foi clicado
      const eventElements = e.target
        .closest("td")
        .querySelectorAll(".event-item");
      eventElements.forEach((eventElement, index) => {
        if (eventElement.contains(e.target)) {
          scheduleIndex = index; // Define o índice com base no evento clicado
        }
      });

      // Se nenhum evento foi clicado, mas há eventos, use o índice 0 como padrão
      if (scheduleIndex === null && events.length > 0) {
        scheduleIndex = 0;
      }

      // Exibe a data e o índice do evento no console para verificação
      console.log("Data selecionada:", date);
      console.log("Índice do evento selecionado:", scheduleIndex);

      // Abre o modal com a data e o índice correto do evento, se houver
      openModal(date, scheduleIndex);
    });
  });
}

function saveSchedule(dateString, scheduleIndex) {
  const dateStart = document.getElementById("date-start").value;
  const dateEnd = document.getElementById("date-end").value;
  const title = document.getElementById("title").value;
  const description = document.getElementById("description").value;
  const time = document.getElementById("time").value;
  const alarm = document.getElementById("alarm").checked;

  const address = {
    cep: document.getElementById("cep").value,
    street: document.getElementById("street").value,
    number: document.getElementById("number").value,
    neighborhood: document.getElementById("neighborhood").value,
    city: document.getElementById("city").value,
    state: document.getElementById("state").value,
    reference: document.getElementById("reference").value,
  };

  // Determinando o ID (autoincremento)
  let newId = 1; // Default to 1 if this is the first schedule for the day
  if (schedules[dateString] && schedules[dateString].length > 0) {
    newId = Math.max(...schedules[dateString].map((s) => s.id || 0)) + 1;
  }

  const schedule = {
    id: newId, // Adicionando o ID autoincrementado
    dateStart,
    dateEnd,
    title,
    description,
    time,
    alarm,
    address,
  };

  // Se o índice do agendamento não for nulo, significa que estamos atualizando um agendamento existente
  if (scheduleIndex !== null) {
    console.log(
      `Atualizando agendamento no índice ${scheduleIndex} para a data ${dateString}`
    );
    schedules[dateString][scheduleIndex] = schedule;
  } else {
    console.log(`Criando novo agendamento para a data ${dateString}`);
    if (!schedules[dateString]) {
      schedules[dateString] = [];
    }
    schedules[dateString].push(schedule);
  }

  console.log("Agendamentos atualizados:", schedules);
  saveSchedulesToLocalStorage();
  console.log("Agendamento salvo com sucesso!");
  closeModal();
}

function removeSchedule(dateString, scheduleIndex) {
  if (schedules[dateString]) {
    schedules[dateString].splice(scheduleIndex, 1);
    if (schedules[dateString].length === 0) {
      delete schedules[dateString];
    }
    saveSchedulesToLocalStorage();
    generateCalendar(currentYear, currentMonth);
  }
}

// Função para abrir o modal
function openModal(dateString, scheduleIndex = null) {
  const modal = document.getElementById("modal");
  modal.style.display = "block";

  // Garantir que o modal abra sempre com o scroll no topo
  modal.scrollTop = 0;

  const dateStartInput = document.getElementById("date-start");
  const dateEndInput = document.getElementById("date-end");
  const titleInput = document.getElementById("title");
  const descriptionInput = document.getElementById("description");
  const timeInput = document.getElementById("time");
  const alarmCheckbox = document.getElementById("alarm");
  const cepInput = document.getElementById("cep");
  const streetInput = document.getElementById("street");
  const numberInput = document.getElementById("number");
  const neighborhoodInput = document.getElementById("neighborhood");
  const cityInput = document.getElementById("city");
  const stateInput = document.getElementById("state");
  const referenceInput = document.getElementById("reference");

  // Logging inputs to check if they are being found correctly
  console.log("Modal elements found:", {
    dateStartInput,
    dateEndInput,
    titleInput,
    descriptionInput,
    timeInput,
    alarmCheckbox,
    cepInput,
    streetInput,
    numberInput,
    neighborhoodInput,
    cityInput,
    stateInput,
    referenceInput,
  });

  if (
    scheduleIndex !== null &&
    schedules[dateString] &&
    schedules[dateString][scheduleIndex]
  ) {
    console.log("Carregando evento existente para edição.");
    const schedule = schedules[dateString][scheduleIndex];

    // Exibe os dados do evento no modal
    dateStartInput.value = schedule.dateStart || "";
    dateEndInput.value = schedule.dateEnd || "";
    titleInput.value = schedule.title || "";
    descriptionInput.value = schedule.description || "";
    timeInput.value = schedule.time || "";
    alarmCheckbox.checked = schedule.alarm || false;
    cepInput.value = schedule.address?.cep || "";
    streetInput.value = schedule.address?.street || "";
    numberInput.value = schedule.address?.number || "";
    neighborhoodInput.value = schedule.address?.neighborhood || "";
    cityInput.value = schedule.address?.city || "";
    stateInput.value = schedule.address?.state || "";
    referenceInput.value = schedule.address?.reference || "";
  } else {
    // Logging que um novo agendamento está sendo criado
    console.log("Criando novo agendamento para a data:", dateString);

    // Limpa os campos do modal para um novo agendamento
    dateStartInput.value = "";
    dateEndInput.value = "";
    titleInput.value = "";
    descriptionInput.value = "";
    timeInput.value = "";
    alarmCheckbox.checked = false;
    cepInput.value = "";
    streetInput.value = "";
    numberInput.value = "";
    neighborhoodInput.value = "";
    cityInput.value = "";
    stateInput.value = "";
    referenceInput.value = "";
  }

  // Logging para confirmar que os ouvintes de eventos estão sendo configurados
  console.log(
    "Configurando ouvintes de eventos para botões de salvar e cancelar"
  );

  document.getElementById("save-btn").onclick = () =>
    saveSchedule(dateString, scheduleIndex);

  document.getElementById("cancel-btn").onclick = () => closeModal();
}

// Evento para abrir o modal em branco quando o botão de adicionar evento for clicado
document.getElementById("add-event-button").onclick = () => {
  console.log("Modal - add-event-button");
  openModal("", null); // Passa `null` para indicar que é um novo evento
};

// Supondo que você tenha um evento de clique nos dias do calendário
function onDateClick(dateString, scheduleIndex) {
  console.log("Modal - onDateClick");
  openModal(dateString, scheduleIndex); // Passa `scheduleIndex` para editar um evento existente
}

// Exemplo de como você poderia chamar `onDateClick` para datas que têm eventos
document.querySelectorAll(".calendar-day").forEach((dayElement) => {
  dayElement.onclick = () => {
    const dateString = dayElement.dataset.date; // Supondo que a data esteja armazenada em um atributo data
    const scheduleIndex = findScheduleIndexForDate(dateString); // Função que deve retornar o índice do agendamento para a data clicada
    onDateClick(dateString, scheduleIndex); // Chama a função para abrir o modal
  };
});

// Função para encontrar o índice do agendamento para uma data específica
function findScheduleIndexForDate(dateString) {
  if (schedules[dateString]) {
    // Retorna o índice do primeiro agendamento encontrado, por exemplo
    return 0; // Você pode ajustar essa lógica conforme necessário
  }
  return null; // Nenhum agendamento encontrado
}

// Adiciona o evento de tecla "Esc"
document.addEventListener("keydown", function (event) {
  if (event.key === "Escape") {
    closeModal();
  }
});

function closeModal() {
  document.getElementById("modal").style.display = "none";
}

document.getElementById("search-btn").addEventListener("click", function () {
  const cep = document.getElementById("cep").value;
  if (cep.length === 8) {
    fetchAddress(cep);
  } else {
    alert("CEP inválido. Verifique e tente novamente.");
  }
});

function fetchAddress(cep) {
  fetch(`https://viacep.com.br/ws/${cep}/json/`)
    .then((response) => response.json())
    .then((data) => {
      if (!data.erro) {
        document.getElementById("street").value = data.logradouro || "";
        document.getElementById("neighborhood").value = data.bairro || "";
        document.getElementById("city").value = data.localidade || "";
        document.getElementById("state").value = data.uf || "";
      } else {
        alert("Endereço não encontrado para o CEP fornecido.");
      }
    })
    .catch((error) => {
      console.error("Erro ao buscar o endereço:", error);
      alert("Erro ao buscar o endereço.");
    });
}

document.getElementById("open-maps").onclick = () => {
  const street = document.getElementById("street").value;
  const number = document.getElementById("number").value;
  const neighborhood = document.getElementById("neighborhood").value;
  const city = document.getElementById("city").value;
  const state = document.getElementById("state").value;

  const address = `${street}, ${number} - ${neighborhood}, ${city} - ${state}, Brasil`;
  const url = `https://www.google.com/maps/search/?api=1&query=${encodeURIComponent(
    address
  )}`;

  window.open(url, "_blank");
};

document.getElementById("open-waze").onclick = () => {
  const street = document.getElementById("street").value;
  const number = document.getElementById("number").value;
  const neighborhood = document.getElementById("neighborhood").value;
  const city = document.getElementById("city").value;
  const state = document.getElementById("state").value;

  const address = `${street}, ${number} - ${neighborhood}, ${city} - ${state}, Brasil`;
  const url = `https://waze.com/ul?q=${encodeURIComponent(address)}`;

  window.open(url, "_blank");
};

// ------------

function handleDateClick(data) {
  console.log("Data clicada:", data); // Log da data clicada

  // Filtrar eventos do dia usando a estrutura de schedules
  const eventosDoDia = schedules[""]
    ? schedules[""].filter((evento) => {
        console.log("Verificando evento:", evento); // Log do evento atual sendo verificado
        return evento.dateStart === data;
      })
    : [];

  console.log("Eventos do dia:", eventosDoDia); // Log dos eventos filtrados

  const eventListDiv = document.getElementById("event-list");
  eventListDiv.innerHTML = ""; // Limpar a lista de eventos

  if (eventosDoDia.length > 0) {
    eventosDoDia.forEach((evento) => {
      // Extrair dia, mês e ano da data de início
      const [year, month, day] = evento.dateStart.split("-");
      console.log(`Data extraída: ${day}-${month}-${year}`); // Log da data extraída

      // Formatar a data usando a função formatDate
      const formattedDate = formatDate(day, month, year);
      console.log("Data formatada:", formattedDate); // Log da data formatada

      // Adicionar o evento formatado à lista
      const eventoDiv = document.createElement("div");
      eventoDiv.innerHTML = `<li>${formattedDate}: ${evento.title} - ${evento.time}</li>`;
      eventListDiv.appendChild(eventoDiv);
    });
  } else {
    console.log("Não há eventos para este dia."); // Log caso não haja eventos
    eventListDiv.innerHTML = "<p>Não há eventos para este dia.</p>";
  }

  const modal = document.getElementById("modal");
  if (modal) {
    modal.style.display = "block"; // Mostrar o modal
    console.log("Modal exibido."); // Log quando o modal é exibido
  } else {
    console.error("Modal não encontrado"); // Log de erro caso o modal não seja encontrado
  }
}

// Fechar o modal se clicar fora da área do conteúdo
// window.onclick = function (event) {
//   const modal = document.getElementById("modal");
//   if (event.target === modal) {
//     closeModal();
//   }
// };
