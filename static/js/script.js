// Ativar links do menu
const links = document.querySelectorAll(".header-menu a");

function ativarLink(link) {
  const url = location.href;
  const href = link.href;

  if (url.includes(href) && url === href) {
    link.classList.add("ativo");
  }
}

links.forEach(ativarLink);

// Ativar Galeria
const filtroGaleria = document.querySelectorAll(".filtro-menu a");

function ativarFiltro(event) {
  const id = event.getAttribute("id");
  const resposta = document.getElementById(id);
  const url = location.href;
  const id_url = url.split("/filtro=");

  console.log(id + "/", id_url[1]);

  if (id + "/" === id_url[1]) {
    resposta.classList.add("filtro-ativo");
  }
}

filtroGaleria.forEach(ativarFiltro);

// Animação
if (window.SimpleAnime) {
  new SimpleAnime();
}
