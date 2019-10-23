//the next coodinate to check

module nextcood (cood,Repeat,coodout)

	input [7:0] cood;
	input [2:0] Repeat;
	
	output [7:0] coodout;
	
	function [7:0] coodtr;
		input [7:0] cood;
		input [2:0] Repeat;
		begin
			case (Repeat)
				3'b000:	coodtr = cood + 8'b00000001 
				3'b001:  coodtr = cood + 8'b00000001 + 8'b00010000
				3'b010:  coodtr = cood               + 8'b00010000
				3'b011:  coodtr = cood - 8'b00000001 + 8'b00010000
				3'b100:  coodtr = cood - 8'b00000001 
				3'b101:  coodtr = cood - 8'b00000001 - 8'b00010000
				3'b110:  coodtr = cood               - 8'b00010000
				3'b111:  coodtr = cood + 8'b00000001 - 8'b00010000
			endcase
		end
	endfunction
	assign coodout = coodtr(cood,Repeat);
endmodule
	