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
  function copySellerToShipper() {
    const sellerFields = ["name", "inn", "kpp", "address", "manager_fio"];
    sellerFields.forEach((field) => {
      const sellerValue = document.querySelector(
        `[name="seller-${field}"]`
      ).value;
      document.querySelector(`[name="shipper-${field}"]`).value = sellerValue;
    });
  }

  function copyBuyerToConsignee() {
    const buyerFields = ["name", "inn", "kpp", "address", "manager_fio"];
    buyerFields.forEach((field) => {
      const buyerValue = document.querySelector(
        `[name="buyer-${field}"]`
      ).value;
      document.querySelector(`[name="consignee-${field}"]`).value = buyerValue;
    });
  }

  document.querySelectorAll('input[type="radio"]').forEach(radio => {
        radio.addEventListener("change", function() {
            if (this.name === "shipper-relation_type" && this.value === "Он же") {
                copySellerToShipper();
            }
            if (this.name === "consignee-relation_type" && this.value === "Он же") {
                copyBuyerToConsignee();
            }
        });
    });
});
