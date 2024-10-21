/*
 * Copyright (c) 2024 Your Name
 * SPDX-License-Identifier: Apache-2.0
 */

`default_nettype none

module tt_um_htfab_mem_test (
    input  wire [7:0] ui_in,    // Dedicated inputs
    output wire [7:0] uo_out,   // Dedicated outputs
    input  wire [7:0] uio_in,   // IOs: Input path
    output wire [7:0] uio_out,  // IOs: Output path
    output wire [7:0] uio_oe,   // IOs: Enable path (active high: 0=input, 1=output)
    input  wire       ena,      // always 1 when the design is powered, so you can ignore it
    input  wire       clk,      // clock
    input  wire       rst_n     // reset_n - low to reset
);

wire we = ui_in[7];
wire [4:0] addr = ui_in[4:0];
wire [7:0] data = uio_in;

reg [7:0] mem [31:0];

always @(posedge clk) begin
    if (we) begin
        mem[addr] <= data;
    end  
end

wire [4:0] addr_inc = addr + 1;

assign uo_out = mem[addr];
assign uio_out = we ? 8'b00000000 : mem[addr_inc];
assign uio_oe = we ? 8'b00000000 : 8'b11111111;

wire _unused = &{ena, rst_n, ui_in[6:5], 1'b0};

endmodule
