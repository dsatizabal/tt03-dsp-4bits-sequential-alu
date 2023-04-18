`timescale 1ns / 1ps

module dsp_4its_seq_alu(input [7:0] io_in, output [7:0] io_out);

   wire clk			    = io_in[7];
   wire reset			= io_in[6];
   wire [3:0]data_in	= io_in[3:0];

   reg [3:0] result;
   reg [3:0] sign_zero_carry_done;
   assign io_out = { sign_zero_carry_done, result };

   reg [3:0] alu_state;
   reg [3:0] op1;
   reg [3:0] op2;
   reg [3:0] operation;

   localparam GET_FIRST_OPERAND         = 4'b0000;
   localparam GET_SECOND_OPERAND        = 4'b0001;
   localparam GET_AND_PERFORM_OPERATION = 4'b0010;

   always @(posedge clk) begin
      if (reset) begin
         alu_state <= GET_FIRST_OPERAND;
         sign_zero_carry_done <= 4'b0000;
      end else begin
         case (alu_state)
            GET_FIRST_OPERAND:
               op1 <= data_in;
               alu_state <= GET_SECOND_OPERAND;
            GET_SECOND_OPERAND:
               op2 <= data_in;
               alu_state <= GET_AND_PERFORM_OPERATION;
            GET_AND_PERFORM_OPERATION:
               operation <= data_in;
               case(operation)
                  4'b0000:
                     if (op1 + op2 > 4'hF) sign_zero_carry_done[1] = 1'b1;
                     result = A + B ;
                  4'b0001:
                     if (op1 < op2) sign_zero_carry_done[3] = 1'b1;
                     if (op1 == op2) sign_zero_carry_done[2] = 1'b1;
                     result = A - B ;
                  4'b0010:
                     if (op1 & op2 > 4'hF) sign_zero_carry_done[1] = 1'b1;
                     if (op1 & op2 == 4'h0) sign_zero_carry_done[2] = 1'b1;
                     result = A & B;
                  4'b0011:
                     if (op1 | op2 > 4'hF) sign_zero_carry_done[1] = 1'b1;
                     if (op1 | op2 == 4'h0) sign_zero_carry_done[2] = 1'b1;
                     result = A | B;
                  4'b0100:
                     if (~op1 > 4'hF) sign_zero_carry_done[1] = 1'b1;
                     if (~op1 == 4'h0) sign_zero_carry_done[2] = 1'b1;
                     result = ~A;
                  4'b0101:
                     if (~(op1 & op2) > 4'hF) sign_zero_carry_done[1] = 1'b1;
                     if (~(op1 & op2) == 4'h0) sign_zero_carry_done[2] = 1'b1;
                     result = A & B;
                  4'b0110:
                     if (~(op1 | op2) > 4'hF) sign_zero_carry_done[1] = 1'b1;
                     if (~(op1 | op2) == 4'h0) sign_zero_carry_done[2] = 1'b1;
                     result = A | B;
                  default:
                    if (op1 + op2 > 4'hF) sign_zero_carry_done[1] = 1'b1;
                    result = A + B ;
               endcase(operation)

                sign_zero_carry_done[0] = 1'b1;
                alu_state <= GET_FIRST_OPERAND;
         endcase(alu_state)
      end
    end

endmodule
