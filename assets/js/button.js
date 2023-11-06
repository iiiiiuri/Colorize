
      const dropdownButton = document.getElementById("dropdown-button");
      const dropdownMenu = document.getElementById("dropdown-menu");

      dropdownButton.addEventListener("click", () => {
        dropdownMenu.classList.toggle("hidden");
      });

      // Feche o dropdown quando clicar fora dele
      document.addEventListener("click", (event) => {
        if (!dropdownButton.contains(event.target)) {
          dropdownMenu.classList.add("hidden");
        }
      });
