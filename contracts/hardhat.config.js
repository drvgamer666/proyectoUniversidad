const { ethers } = require("hardhat");

async function main() {
  // Configura dos proveedores JSON-RPC para simular dos nodos diferentes
  const provider1 = new ethers.providers.JsonRpcProvider("http://127.0.0.1:8545");
  const provider2 = new ethers.providers.JsonRpcProvider("http://127.0.0.1:8546");

  // Crea dos carteras con claves privadas y los proveedores configurados
  const wallet1 = new ethers.Wallet("PRIVATE_KEY_1", provider1);
  const wallet2 = new ethers.Wallet("PRIVATE_KEY_2", provider2);

  // Despliega el contrato usando la primera cartera y proveedor
  const SimpleBank = await ethers.getContractFactory("SimpleBank", wallet1);
  const bank = await SimpleBank.deploy();
  await bank.deployed();
  console.log(`Contrato desplegado en la dirección: ${bank.address}`);

  // Interactúa con el contrato usando la segunda cartera y proveedor
  const balanceBefore = await bank.connect(wallet2).getBalance();
  console.log(`Balance antes del depósito: ${balanceBefore.toString()}`);

  // Realiza un depósito de 1 Ether desde la segunda cartera
  const tx = await bank.connect(wallet2).deposit({ value: ethers.utils.parseEther("1.0") });
  await tx.wait();

  // Verifica el balance después del depósito
  const balanceAfter = await bank.connect(wallet2).getBalance();
  console.log(`Balance después del depósito: ${balanceAfter.toString()}`);
}

main()
  .then(() => process.exit(0))
  .catch(error => {
    console.error(error);
    process.exit(1);
  });
