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



  document.getElementById("show-section-form").onclick = function () {
    document.getElementById("new-section-form").style.display = "block";
  };

  // Обработка формы
  document.getElementById("section-form").onsubmit = async function (e) {
    e.preventDefault();
    
    const formData = new FormData(this);

    const response = await fetch("{% url 'create_section_ajax' %}", {
      method: "POST",
      body: formData,
      headers: {
        'X-CSRFToken': formData.get('csrfmiddlewaretoken')
      }
    });

    if (response.ok) {
      const data = await response.json();

      // Добавляем новый раздел в select
      const select = document.getElementById("id_section");
      const option = new Option(data.name, data.id);
      option.selected = true;
      select.add(option);

      // Скрыть и сбросить форму
      this.reset();
      document.getElementById("new-section-form").style.display = "none";
    } else {
      alert("Ошибка при добавлении раздела");
    }
  };
