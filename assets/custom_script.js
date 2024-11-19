 // Wait for the DOM to load before running the script
 document.addEventListener("DOMContentLoaded", function () {

    // Tuition fee data for each major (from the cleaned Excel data)
    const tuitionFees = {
      "Medicine (English)": {"listFee": 40000, "advanceFee": 36000},
      "Medicine (30% English)": {"listFee": 30000, "advanceFee": 27000},
      "Dentistry (English)": {"listFee": 32000, "advanceFee": 28800},
      "Dentistry (30% English 70% Turkish)": {"listFee": 30000, "advanceFee": 27000},
      "Pharmacy (English)": {"listFee": 18000, "advanceFee": 16200},
      "Pharmacy (Turkish)": {"listFee": 14000, "advanceFee": 12600},
      "Law (30% English)": {"listFee": 10000, "advanceFee": 9000},
      "Nursing (English)": {"listFee": 7000, "advanceFee": 6300},
      "Nursing (Turkish)": {"listFee": 7000, "advanceFee": 6300},
      "Physiotherapy and Rehabilitation (English)": {"listFee": 7000, "advanceFee": 6300},
      "Physiotherapy and Rehabilitation (Turkish)": {"listFee": 7000, "advanceFee": 6300},
      "Nutrition and Dietetics (Turkish)": {"listFee": 5500, "advanceFee": 4950},
      "Health Management (English)": {"listFee": 5500, "advanceFee": 4950},
      "Health Management (Turkish)": {"listFee": 5500, "advanceFee": 4950},
      "Audiology (Turkish)": {"listFee": 5500, "advanceFee": 4950},
      "Orthotics and Prosthetics (Turkish)": {"listFee": 5500, "advanceFee": 4950},
      "Child Development (Turkish)": {"listFee": 5500, "advanceFee": 4950},
      "Midwifery (Turkish)": {"listFee": 5500, "advanceFee": 4950},
      "Ergotherapy (Turkish)": {"listFee": 5500, "advanceFee": 4950},
      "Social Services (Turkish)": {"listFee": 5500, "advanceFee": 4950},
               "English Teaching 100% Englisht": {"listFee": 5000, "advanceFee": 4500},
      "Speech and Language Therapy (English)": {"listFee": 5500, "advanceFee": 4950},
      "Speech and Language Therapy (Turkish)": {"listFee": 5500, "advanceFee": 4950},
      "Electrical-Electronic Engineering (English)": {"listFee": 6500, "advanceFee": 5850},
      "Biomedical Engineering (English)": {"listFee": 7000, "advanceFee": 6300},
      "Industrial Engineering (English)": {"listFee": 5500, "advanceFee": 4950},
      "Computer Engineering (English)": {"listFee": 7000, "advanceFee": 6300},
      "Civil Engineering (English)": {"listFee": 6500, "advanceFee": 5850},
      "Civil Engineering (Turkish)": {"listFee": 5000, "advanceFee": 4500},
      "Business Administration (English)": {"listFee": 5500, "advanceFee": 4950},
      "Economics and Finance (English)": {"listFee": 5500, "advanceFee": 4950},
      "International Trade and Finance (English)": {"listFee": 5500, "advanceFee": 4950},
      "International Trade and Finance (Turkish)": {"listFee": 5500, "advanceFee": 4950},
      "Management Information Systems (English)": {"listFee": 5500, "advanceFee": 4950},
      "Management Information Systems (Turkish)": {"listFee": 5500, "advanceFee": 4950},
      "Logistic Management (English)": {"listFee": 5500, "advanceFee": 4950},
      "Logistic Management (Turkish)": {"listFee": 5500, "advanceFee": 4950},
      "Human Resources Management (Turkish)": {"listFee": 5500, "advanceFee": 4950},
      "Aviation Management (Turkish)": {"listFee": 5500, "advanceFee": 4950},
      "Banking and Insurance (Turkish)": {"listFee": 5500, "advanceFee": 4950},
      "Psychology (English)": {"listFee": 5500, "advanceFee": 4950},
      "Psychology (Turkish)": {"listFee": 5500, "advanceFee": 4950},
      "Political Science and International Relations (English)": {"listFee": 5500, "advanceFee": 4950},
      "Political Science and Public Administration (English)": {"listFee": 5500, "advanceFee": 4950},
      "Political Science and Public Administration (Turkish)": {"listFee": 5500, "advanceFee": 4950},
      "Architecture (English)": {"listFee": 5000, "advanceFee": 4500},
      "Architecture (Turkish)": {"listFee": 5000, "advanceFee": 4500},
      "Industrial Design (Turkish)": {"listFee": 5000, "advanceFee": 4500},
      "Interior Architecture and Environmental Design (English)": {"listFee": 5000, "advanceFee": 4500},
      "Interior Architecture and Environmental Design (Turkish)": {"listFee": 5000, "advanceFee": 4500},
      "Visual Communication Design (Turkish)": {"listFee": 5000, "advanceFee": 4500},
      "(Turkish) Music Art (Turkish)": {"listFee": 5000, "advanceFee": 4500},
      "Gastronomy and Culinary Arts (Turkish)": {"listFee": 5000, "advanceFee": 4500},
      "Urban Design and Landscape Architecture (Turkish)": {"listFee": 5000, "advanceFee": 4500},
      "Psychological Counselling and Guidance (English)": {"listFee": 5000, "advanceFee": 4500},
      "Psychological Counselling and Guidance (Turkish)": {"listFee": 5000, "advanceFee": 4500},
      "(English) Teaching (English)": {"listFee": 5000, "advanceFee": 4500},
      "Primary Mathematics Teaching (Turkish)": {"listFee": 5000, "advanceFee": 4500},
      "Special Education Teaching (Turkish)": {"listFee": 5000, "advanceFee": 4500},
      "Preschool Teaching (Turkish)": {"listFee": 5000, "advanceFee": 4500},
      "Journalism (Turkish)": {"listFee": 5000, "advanceFee": 4500},
      "Public Relations and Advertising (English)": {"listFee": 5000, "advanceFee": 4500},
      "Public Relations and Advertising (Turkish)": {"listFee": 5000, "advanceFee": 4500},
      "Media and Visual Arts (Turkish)": {"listFee": 5000, "advanceFee": 4500},
      "New Media and Communication (Turkish)": {"listFee": 5000, "advanceFee": 4500},
      "Radio Television and Cinema (Turkish)": {"listFee": 5000, "advanceFee": 4500},
      "Nutrition and Dietetics (Turkish)": {"listFee": 5000, "advanceFee": 4500},
      "Child Development (Turkish) (Haliç Campus) (Turkish)": {"listFee": 5000, "advanceFee": 4500},
      "Midwifery (Haliç Campus) (Turkish)": {"listFee": 5000, "advanceFee": 4500},
      "Physiotherapy and Rehabilitation (Haliç Campus) (Turkish)": {"listFee": 5000, "advanceFee": 4500},
      "Audiology (Turkish)": {"listFee": 5000, "advanceFee": 4500},
      "Social Services (Turkish)": {"listFee": 5000, "advanceFee": 4500},
      "Justice (Turkish)": {"listFee": 3500, "advanceFee": 2800},
      "Oral and Dental Health (Turkish)": {"listFee": 3500, "advanceFee": 3150},
      "Operating Room Services (Turkish)": {"listFee": 3500, "advanceFee": 3150},
      "Anesthesia (English)": {"listFee": 4000, "advanceFee": 3600},
      "Anesthesia (Turkish)": {"listFee": 3500, "advanceFee": 3150},
      "Dental Prosthetics Technology (Turkish)": {"listFee": 4000, "advanceFee": 3600},
      "Child Development (Turkish)": {"listFee": 3500, "advanceFee": 3150},
      "Dental Prosthesis Technology (Turkish)": {"listFee": 4000, "advanceFee": 3600},
      "Dialysis (Turkish)": {"listFee": 3500, "advanceFee": 3150},
      "Pharmacy Services (Turkish)": {"listFee": 3500, "advanceFee": 3150},
      "Electroneurophysiology (Turkish)": {"listFee": 3500, "advanceFee": 3150},
      "Physiotherapy (English)": {"listFee": 3500, "advanceFee": 3150},
      "Physiotherapy (Turkish)": {"listFee": 3500, "advanceFee": 3150},
      "First and Emergency Aid (English)": {"listFee": 4000, "advanceFee": 3600},
      "First and Emergency Aid (Turkish)": {"listFee": 3500, "advanceFee": 3150},
      "Occupational Health and Safety (Turkish)": {"listFee": 3500, "advanceFee": 3150},
      "Audiometry (Turkish)": {"listFee": 3500, "advanceFee": 3150},
      "Opticianry (Turkish)": {"listFee": 3500, "advanceFee": 3150},
      "Pathology Laboratory Techniques (Turkish)": {"listFee": 3500, "advanceFee": 3150},
      "Radiotherapy (Turkish)": {"listFee": 3500, "advanceFee": 3150},
      "Prosthetics and Orthotics (Turkish)": {"listFee": 3500, "advanceFee": 3150},
      "Management of Health Institutions (Turkish)": {"listFee": 3500, "advanceFee": 3150},
      "Medical Documentation and Secretary (Turkish)": {"listFee": 3500, "advanceFee": 3150},
      "Medical Imaging Techniques (Turkish)": {"listFee": 3500, "advanceFee": 3150},
      "Medical Laboratory Techniques (Turkish)": {"listFee": 3500, "advanceFee": 3150},
      "Oral and Dental Health (Turkish)": {"listFee": 3500, "advanceFee": 3150},
      "Operation Room Service (Turkish)": {"listFee": 3500, "advanceFee": 3150},
      "Anesthesia (Turkish)": {"listFee": 3500, "advanceFee": 3150},
      "Computer Programming (Turkish)": {"listFee": 3500, "advanceFee": 3150},
      "Child Development (Turkish)": {"listFee": 3500, "advanceFee": 3150},
      "Biomedical Device Technology (Turkish)": {"listFee": 3500, "advanceFee": 3150},
      "Dental Prosthesis Technology (Haliç)	": {"listFee": 3500, "advanceFee": 3150},
      "Dialysis (Turkish)": {"listFee": 3500, "advanceFee": 3150},
      "Electroneurophysiology (Turkish)": {"listFee": 3500, "advanceFee": 3150},
      "physiotherapy (Turkish)": {"listFee": 3500, "advanceFee": 3150},
      "Interior Design (Turkish)": {"listFee": 3500, "advanceFee": 3150},
      "First and emergency Aid (Turkish)": {"listFee": 3500, "advanceFee": 3150},
      "Construction Technology (Turkish)": {"listFee": 3500, "advanceFee": 3150},
      "Occiptional Health and Safety (Turkish)": {"listFee": 3500, "advanceFee": 3150},
      "Architectural Restoration (Turkish)": {"listFee": 3500, "advanceFee": 3150},
      "Audiometry (Turkish)": {"listFee": 3500, "advanceFee": 3150},
      "Opticianry (Turkish)": {"listFee": 3500, "advanceFee": 3150},
      "Civil Aviation Transportation Management (Turkish)": {"listFee": 3500, "advanceFee": 3150},
      "Management of Health Institutions (Turkish)": {"listFee": 3500, "advanceFee": 3150},
      "Medical Documentation and Secretary (Turkish)": {"listFee": 3500, "advanceFee": 3150},
      "Medical Imaging Techniques (Turkish)": {"listFee": 3500, "advanceFee": 3150},
      "Medical Laboratory Techniques (Turkish)": {"listFee": 3500, "advanceFee": 3150},
      "Foreign Trade": {"listFee": 3500, "advanceFee": 3150},
      "Banking and Insurance (Turkish)": {"listFee": 3500, "advanceFee": 3150},
      "Foreign Trade (Turkish)": {"listFee": 3500, "advanceFee": 3150},
      "Public Relations and Publicity (Turkish)": {"listFee": 3500, "advanceFee": 3150},
      "Human Resources Management (Turkish)": {"listFee": 3500, "advanceFee": 3150},
      "Business Administration (Turkish)": {"listFee": 3500, "advanceFee": 3150},
      "Logistics (Turkish)": {"listFee": 3500, "advanceFee": 3150},
      "Finance (Turkish)": {"listFee": 3500, "advanceFee": 3150},
      "Accounting and Taxation (Turkish)": {"listFee": 3500, "advanceFee": 3150},
      "Radio and Television Programming (Turkish)": {"listFee": 3500, "advanceFee": 3150},
      "Civil Aviation Cabin Services": {"listFee": 3500, "advanceFee": 3150},
      "Social Services (Turkish)": {"listFee": 3500, "advanceFee": 3150},
      "Sports Management (Turkish)": {"listFee": 3500, "advanceFee": 3150},
      "Applied English and Translation (English)": {"listFee": 3500, "advanceFee": 3150},
      "English Language Teaching (English)": {"listFee": 4500, "advanceFee": 4050},
      "Pre-School Teaching (Turkish)": {"listFee": 1200, "advanceFee": 1200},


    };

    // List of special countries with 15% discount
    const specialCountries = [
        "Afghanistan", "Albania", "Algeria", "Azerbaijan", "Bangladesh", "Belarus",
        "Bosnia and Herzegovina", "Brazil", "Bulgaria", "Cameroon", "Chile", "Comoros",
        "Congo", "Croatia", "Democratic Republic of Congo", "Djibouti", "Egypt",
        "Georgia", "Greece", "India", "Indonesia", "Israel", "Jordan", "Kazakhstan",
        "Kenya", "Kosovo", "Kyrgyzstan", "Lebanon", "Malaysia", "Mali", "Mauritania",
        "Moldova", "Mongolia", "Montenegro", "Morocco", "Myanmar", "Nigeria", "North Macedonia",
        "Pakistan", "Palestine", "Peru", "Romania", "Russia", "Senegal", "Serbia",
        "Sierra Leone", "Somalia", "Sudan", "Tajikistan", "Tanzania", "Tunisia",
        "Ukraine", "Uzbekistan"
    ];

    // Included Turkish countries for 4-year programs (15% discount)
    const includedTurkishCountries = [
        "Bahrain", "United Arab Emirates", "Iraq", "Qatar", "Comoros", "Kuwait",
        "Libya", "Saudi Arabia", "Syria", "Oman", "Yemen"
    ];

    // Excluded Turkish programs (Medicine, Dentistry, Pharmacy, Physiotherapy, Law)
    const excludedTurkishPrograms = ["Medicine", "Dentistry", "Pharmacy", "Physiotherapy", "Law"];

    // Campaign Discounts (without nationality conditions)
    const campaigns = {
        "Biomedical Engineering English": 15,
        "Electrical-Electronic Engineering English": 15,
        "Nursing English": 15,
        "Architecture English": 15,
        // The following will be handled conditionally in calculateRevenue
        "Medicine Turkish": 0,
        "Pharmacy English": 0
    };


    /// Event listener for the calculate button
    document.getElementById("calculateButton").addEventListener("click", calculateRevenue);

    // Event listener for Excel upload
    document.getElementById('excelFile').addEventListener('change', handleFileUpload);

    function handleFileUpload(event) {
        var file = event.target.files[0];
        if (!file) return;

        var reader = new FileReader();
        reader.onload = function (e) {
            var data = new Uint8Array(e.target.result);
            var workbook = XLSX.read(data, { type: 'array' });
            var worksheet = workbook.Sheets[workbook.SheetNames[0]];
            var jsonData = XLSX.utils.sheet_to_json(worksheet, { header: 1 });
            processExcelData(jsonData);
        };
        reader.readAsArrayBuffer(file);
    }

    function processExcelData(data) {
        var tableBody = document.getElementById('tuitionTable').getElementsByTagName('tbody')[0];
        tableBody.innerHTML = '';
        const headers = data[0];
        const programIndex = headers.indexOf('Program');
        const nationalityIndex = headers.indexOf('Nationality');

        if (programIndex === -1 || nationalityIndex === -1) {
            alert('Excel file must contain "Program" and "Nationality" columns.');
            return;
        }

        for (let i = 1; i < data.length; i++) {
            const rowData = data[i];
            const program = rowData[programIndex]?.trim();
            const nationality = rowData[nationalityIndex]?.trim();

            if (program && nationality) {
                const numStudents = parseInt(rowData[headers.indexOf('Number of Students')]) || 1;
                const discount = calculateAutomaticDiscount(nationality, program);
                addRowFromExcel(program, nationality, numStudents, discount);
            }
        }

        calculateRevenue();
    }
function addRowFromExcel(program, nationality, numStudents, discount) {
        var table = document.getElementById('tuitionTable').getElementsByTagName('tbody')[0];
        var row = table.insertRow();

        row.insertCell(0).innerHTML = program;
        row.insertCell(1).innerHTML = nationality;
        row.insertCell(2).innerHTML = program.includes("English") ? "English" : "Turkish";

        var grossTuitionCell = row.insertCell(3);
        grossTuitionCell.className = 'grossTuition';
        grossTuitionCell.innerHTML = tuitionFees[program]?.listFee || '0.00';

        var numStudentsCell = row.insertCell(4);
        var numStudentsInput = document.createElement('input');
        numStudentsInput.type = 'number';
        numStudentsInput.className = 'numStudentsInput';
        numStudentsInput.value = numStudents;
        numStudentsInput.onchange = calculateRevenue;
        numStudentsCell.appendChild(numStudentsInput);

        row.insertCell(5).className = 'netFee';
        var discountCell = row.insertCell(6);
        var discountInput = document.createElement('input');
        discountInput.type = 'number';
        discountInput.className = 'discountInput';
        discountInput.step = '1';
        discountInput.min = '0';
        discountInput.max = '50';
        discountInput.value = discount;
        discountInput.onchange = calculateRevenue;
        discountCell.appendChild(discountInput);

        row.insertCell(7).className = 'totalRevenue';
        row.insertCell(8).className = 'discountedRevenue';
        row.insertCell(9).className = 'advanceFeeRevenue';
    }

    function calculateAutomaticDiscount(nationality, program) {
        let discount = 0;
        if (specialCountries.includes(nationality)) discount += 15;
        // Additional logic for discounts can be added here
        return Math.min(discount, 50);
    }

    function calculateRevenue() {
        var table = document.getElementById('tuitionTable').getElementsByTagName('tbody')[0];
        var rows = table.rows;
        var totalRevenueSum = 0;
        var totalStudentsCount = 0;

        for (var i = 0; i < rows.length; i++) {
            var row = rows[i];
            var grossTuition = parseFloat(row.cells[3].innerHTML) || 0;
            var numStudents = parseInt(row.querySelector('.numStudentsInput').value) || 0;
            var discountPercentage = parseInt(row.querySelector('.discountInput').value) || 0;

            var finalFee = grossTuition - (grossTuition * discountPercentage / 100);
            var totalRevenue = finalFee * numStudents;

            var advanceFee = tuitionFees[row.cells[0].innerHTML]?.advanceFee || 0;
            var advanceFeeRevenue = advanceFee * numStudents;
            var discountedRevenue = grossTuition * (discountPercentage / 100) * numStudents;

            row.querySelector('.netFee').innerHTML = finalFee.toFixed(2);
            row.querySelector('.totalRevenue').innerHTML = totalRevenue.toFixed(2);
            row.querySelector('.discountedRevenue').innerHTML = discountedRevenue.toFixed(2);
            row.querySelector('.advanceFeeRevenue').innerHTML = advanceFeeRevenue.toFixed(2);

            totalRevenueSum += totalRevenue;
            totalStudentsCount += numStudents;
        }

        document.getElementById('avgRevenue').innerHTML = totalRevenueSum.toFixed(2);
        document.getElementById('totalStudents').innerHTML = totalStudentsCount;
    }

    // Add an initial empty row
    addRow();

    function addRow() {
        var table = document.getElementById('tuitionTable').getElementsByTagName('tbody')[0];
        var row = table.insertRow();
        row.insertCell(0).innerHTML = 'Select Program';
        row.insertCell(1).innerHTML = 'Select Nationality';
        row.insertCell(2).innerHTML = 'English';
        row.insertCell(3).className = 'grossTuition';
        row.insertCell(3).innerHTML = '0.00';

        var numStudentsCell = row.insertCell(4);
        var numStudentsInput = document.createElement('input');
        numStudentsInput.type = 'number';
        numStudentsInput.className = 'numStudentsInput';
        numStudentsInput.value = 1;
        numStudentsInput.onchange = calculateRevenue;
        numStudentsCell.appendChild(numStudentsInput);

        row.insertCell(5).className = 'netFee';
        var discountCell = row.insertCell(6);
        var discountInput = document.createElement('input');
        discountInput.type = 'number';
        discountInput.className = 'discountInput';
        discountInput.step = '1';
        discountInput.min = '0';
        discountInput.max = '50';
        discountInput.value = 0;
        discountInput.onchange = calculateRevenue;
        discountCell.appendChild(discountInput);

        row.insertCell(7).className = 'totalRevenue';
        row.insertCell(8).className = 'discountedRevenue';
        row.insertCell(9).className = 'advanceFeeRevenue';
    }
});