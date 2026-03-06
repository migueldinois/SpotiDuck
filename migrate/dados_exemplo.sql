INSERT INTO `spotiduck`.`genero` (`nome`, `url_icone`, `cor`) 
VALUES 
("Rock", "https://cdn-icons-png.flaticon.com/512/2131/2131878.png", "red"),
("Pop", "", "blue"),
("MPB", "", "#FACADA");

INSERT INTO `spotiduck`.`musicas` 
(`img_capa`, `nome`, `cantor`, `duracao`, `nome_genero`, ativo) 
VALUES 
("https://akamai.sscdn.co/uploadfile/letras/fotos/5/4/1/6/5416d9ee2db3cf86b60997a55820c41a-tb7.jpg", 
"Sweet Child O' Mine", 
"Guns N' Roses", 
"00:05:02",
"Rock",
1),

("https://akamai.sscdn.co/uploadfile/letras/fotos/d/3/b/b/d3bb3024303d4a7e09d3cafef095de0c-tb7.jpg",
"Ordinary",
"Alex Warren",
"00:03:06",
"Pop",
1),

("https://upload.wikimedia.org/wikipedia/pt/8/84/Lu%C3%ADsa_Sonza_-_Devagarinho.png", 
"Devagarinho", 
"Luisa Sonza", 
"00:03:12",
"MPB",
1);

