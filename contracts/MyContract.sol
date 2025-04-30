// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SimpleBank {
    // Mapeo que almacena los balances de los usuarios
    mapping(address => uint256) public balances;

    // Evento que se emite cuando un depósito es realizado
    event DepositMade(address indexed accountAddress, uint256 amount);

    // Evento que se emite cuando un retiro es realizado
    event WithdrawalMade(address indexed accountAddress, uint256 amount);

    // Función para realizar un depósito de Ether
    function deposit() public payable {
        // Se incrementa el balance del usuario
        balances[msg.sender] += msg.value;

        // Se emite el evento de depósito
        emit DepositMade(msg.sender, msg.value);
    }

    // Función para retirar Ether del contrato
    function withdraw(uint256 amount) public {
        // Verifica que el usuario tenga suficientes fondos
        require(balances[msg.sender] >= amount, "Fondos insuficientes");

        // Decrementa el balance del usuario
        balances[msg.sender] -= amount;

        // Transfiere el Ether al usuario
        payable(msg.sender).transfer(amount);

        // Emite el evento de retiro
        emit WithdrawalMade(msg.sender, amount);
    }

    // Función para consultar el balance de un usuario
    function getBalance() public view returns (uint256) {
        return balances[msg.sender];
    }
}
