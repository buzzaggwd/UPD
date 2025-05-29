// $("#add-section-btn").click(function () {
//   $("#section-modal").modal("show");
// });

// $("#section-form").submit(function (e) {
//   e.preventDefault();
//   $.ajax({
//     type: "POST",
//     url: "/add_section/",
//     data: $(this).serialize(),
//     success: function (response) {
//       $("#product-section").append(
//         `<option value="${response.id}">${response.name}</option>`
//       );
//       $("#section-modal").modal("hide");
//     },
//   });
// });

document.addEventListener("DOMContentLoaded", function () {
    function copyFields(fromPrefix, toPrefix, fields) {
        fields.forEach(field => {
            const fromInput = document.querySelector(`input[name="${fromPrefix}-${field}"]`);
            const toInput = document.querySelector(`input[name="${toPrefix}-${field}"]`);
            if (fromInput && toInput) {
                toInput.value = fromInput.value;
            }
        });
    }

    function clearFields(prefix, fields) {
        fields.forEach(field => {
            const input = document.querySelector(`input[name="${prefix}-${field}"]`);
            if (input) {
                input.value = "";
            }
        });
    }

    function handleRelationRadios(radioName, fromPrefix, toPrefix, fields) {
        const radios = document.querySelectorAll(`input[name="${radioName}"]`);
        radios.forEach(radio => {
            radio.addEventListener("change", function () {
                if (this.value === "Он же") {
                    copyFields(fromPrefix, toPrefix, fields);
                } else {
                    clearFields(toPrefix, fields);
                }
            });
        });
    }

    handleRelationRadios("shipper-relation_type", "seller", "shipper", ["name", "inn", "kpp", "address", "manager_fio"]);
    handleRelationRadios("consignee-relation_type", "buyer", "consignee", ["name", "inn", "kpp", "address", "manager_fio"]);
});


