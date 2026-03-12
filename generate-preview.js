const { Resvg } = require("@resvg/resvg-js");
const fs = require("fs");
const path = require("path");

/**
 * Generates a PNG preview image of the Food Checker application using Satori.
 *
 * Satori renders a markup tree (sidebar + product price table) to SVG, and
 * @resvg/resvg-js converts the SVG to PNG. The output is saved to
 * Site/img/food-checker-preview.png.
 *
 * Font paths can be customised via FONT_REGULAR and FONT_BOLD environment
 * variables. When unset, the script falls back to the Lato fonts commonly
 * found on Ubuntu/Debian systems.
 *
 * @throws {Error} If the configured font files cannot be read.
 */
async function generateImage() {
  const fontPath =
    process.env.FONT_REGULAR ||
    "/usr/share/fonts/truetype/lato/Lato-Regular.ttf";
  const fontBoldPath =
    process.env.FONT_BOLD ||
    "/usr/share/fonts/truetype/lato/Lato-Bold.ttf";
  const fontData = fs.readFileSync(fontPath);
  const fontBoldData = fs.readFileSync(fontBoldPath);

  const products = [
    { name: "Arroz Broto Legal 7 Grãos Integral", price: "R$11,49" },
    { name: "Arroz Tio João Tipo 1 5Kg", price: "R$28,99" },
    { name: "Feijão Carioca Kicaldo 1Kg", price: "R$7,99" },
    { name: "Açúcar Cristal União 1Kg", price: "R$4,89" },
    { name: "Óleo de Soja Liza 900ml", price: "R$7,49" },
    { name: "Farinha de Trigo Dona Benta 1Kg", price: "R$5,29" },
  ];

  const markup = {
    type: "div",
    props: {
      style: {
        display: "flex",
        flexDirection: "row",
        width: "1200px",
        height: "630px",
        backgroundColor: "#ffffff",
        fontFamily: "Lato",
      },
      children: [
        // Sidebar
        {
          type: "div",
          props: {
            style: {
              display: "flex",
              flexDirection: "column",
              width: "280px",
              backgroundColor: "#1a1a2e",
              color: "#ffffff",
              padding: "30px 20px",
              alignItems: "center",
            },
            children: [
              {
                type: "div",
                props: {
                  style: {
                    display: "flex",
                    flexDirection: "column",
                    alignItems: "center",
                    marginBottom: "30px",
                  },
                  children: [
                    {
                      type: "div",
                      props: {
                        style: {
                          fontSize: "28px",
                          fontWeight: "bold",
                          color: "#4ecca3",
                          marginBottom: "8px",
                        },
                        children: "🛒 FOOD",
                      },
                    },
                    {
                      type: "div",
                      props: {
                        style: {
                          fontSize: "28px",
                          fontWeight: "bold",
                          color: "#4ecca3",
                        },
                        children: "CHECKER",
                      },
                    },
                  ],
                },
              },
              // Menu items
              ...["Sobre", "Arroz", "Feijão", "Açúcar", "Óleo", "Farinha"].map(
                (item) => ({
                  type: "div",
                  props: {
                    style: {
                      display: "flex",
                      width: "100%",
                      padding: "12px 16px",
                      fontSize: "16px",
                      color: "#cccccc",
                      borderBottom: "1px solid #2a2a4a",
                    },
                    children: item,
                  },
                })
              ),
            ],
          },
        },
        // Main content
        {
          type: "div",
          props: {
            style: {
              display: "flex",
              flexDirection: "column",
              flex: 1,
              padding: "30px 40px",
              backgroundColor: "#f8f9fa",
            },
            children: [
              // Title
              {
                type: "div",
                props: {
                  style: {
                    fontSize: "32px",
                    fontWeight: "bold",
                    color: "#1a1a2e",
                    marginBottom: "6px",
                  },
                  children: "FOOD CHECKER",
                },
              },
              {
                type: "div",
                props: {
                  style: {
                    fontSize: "14px",
                    color: "#666666",
                    marginBottom: "24px",
                  },
                  children:
                    "Comparação de preços de produtos básicos — Marília/SP",
                },
              },
              // Table header
              {
                type: "div",
                props: {
                  style: {
                    display: "flex",
                    flexDirection: "row",
                    backgroundColor: "#1a1a2e",
                    color: "#ffffff",
                    padding: "10px 16px",
                    fontSize: "14px",
                    fontWeight: "bold",
                    borderRadius: "6px 6px 0 0",
                  },
                  children: [
                    {
                      type: "div",
                      props: {
                        style: { flex: 1 },
                        children: "Produto",
                      },
                    },
                    {
                      type: "div",
                      props: {
                        style: { width: "120px", textAlign: "right" },
                        children: "Preço",
                      },
                    },
                  ],
                },
              },
              // Table rows
              ...products.map((product, index) => ({
                type: "div",
                props: {
                  style: {
                    display: "flex",
                    flexDirection: "row",
                    padding: "10px 16px",
                    fontSize: "14px",
                    backgroundColor: index % 2 === 0 ? "#ffffff" : "#f0f0f0",
                    borderBottom: "1px solid #e0e0e0",
                  },
                  children: [
                    {
                      type: "div",
                      props: {
                        style: { flex: 1, color: "#333333" },
                        children: product.name,
                      },
                    },
                    {
                      type: "div",
                      props: {
                        style: {
                          width: "120px",
                          textAlign: "right",
                          color: "#4ecca3",
                          fontWeight: "bold",
                        },
                        children: product.price,
                      },
                    },
                  ],
                },
              })),
              // Footer caption
              {
                type: "div",
                props: {
                  style: {
                    display: "flex",
                    flexDirection: "row",
                    justifyContent: "space-between",
                    marginTop: "20px",
                    fontSize: "12px",
                    color: "#999999",
                  },
                  children: [
                    {
                      type: "div",
                      props: {
                        children: "Supermercado Tauste • Marília/SP",
                      },
                    },
                    {
                      type: "div",
                      props: {
                        children: "FATEC Shunji Nishimura — Big Data em Agronegócio",
                      },
                    },
                  ],
                },
              },
            ],
          },
        },
      ],
    },
  };

  const satori = (await import("satori")).default;

  const svg = await satori(markup, {
    width: 1200,
    height: 630,
    fonts: [
      {
        name: "Lato",
        data: fontData,
        weight: 400,
        style: "normal",
      },
      {
        name: "Lato",
        data: fontBoldData,
        weight: 700,
        style: "normal",
      },
    ],
  });

  const resvg = new Resvg(svg, {
    fitTo: { mode: "width", value: 1200 },
  });
  const pngData = resvg.render();
  const pngBuffer = pngData.asPng();

  const outputPath = path.join(__dirname, "Site", "img", "food-checker-preview.png");
  fs.writeFileSync(outputPath, pngBuffer);
  console.log(`Image generated: ${outputPath}`);
}

generateImage().catch(console.error);
