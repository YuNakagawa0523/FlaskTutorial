// 3 colors LED othello

module othello(
    input     [8:0]  push
	 output    [127:0]  fieldoutput
	);

	reg   [199:0]  field;
	reg   [4:0] Count;
	reg   [7:0] cood;
	reg   [7:0] coodi;
	reg   [3:0] Repeat;
	reg   [2:0] vecl; //vector length
	reg   turn; //whether black or white turn 
	reg   [1:0] tcolor;
	reg   [5:0] sum10;
	reg   [5:0] sum01;
	
	wire       carryout
	wire       coodnext
	wire       color
	
   begin  // when starting the program
       field <= 200'b0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000100100000000000001100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000;
		 turn <= 1'b0
		 vecl <= 3'b000
	end
	
	always @ (posedge push[8]) begin  
	flipcount <= 5'b0
	coodi <= push[7:0]
	cood <= coodi
	vecl <= 3'b000
	if (turn == 1) begin     //the turn of 10

		 //changing the field when putting the piece

		 Repeat <= 4'b0000;
		 while (Repeat != 4'b1000) begin  // checking for 8 directions
			  nextcood(cood,Repeat,coodout);  //
			  assign coodnext = coodout;
			  xyBIN8tofvalue(coodnext,field,fvalue);  //check the next color
			  assign color = fvalue;  //'color' is the color of the next coodinate
			  vecl <=0;
			  Count <=0;

			  //conditional branch
			  if (color == 2'b01) begin  // keep on checking
					cood <= coodnext;
					vecl <= vecl + 3'b1;
			  end
			  else begin
					if (color == 2'b10 and vecl > 0) begin  // if able to flip
						 cood <= coodi;
						 count <= count + vecl;
						 while (vecl > 0) begin         //
							  nextcood(cood,Repeat,coodout);
							  assign coodnext = coodout;
							  assign color = 2'b10;
							  changefield(field,coodnext,color,fieldout);
							  field <= fieldout;
							  vecl <= vecl - 1;           // changing field
						 end
					end
					Repeat <= Repeat + 4'b1;     // move to the next direction
					cood <= coodi;
					vecl <= 0;
			  end
		 end

		 // changeing the field so as to wait for putting a piece

		 Repeat <= 4'b0000;
		 while (Repeat != 4'b1000) begin
			  nextcood(coodi,Repeat,coodout);  // checking for 8 directions
			  assign coodnext = coodout;
			  xyBIN8tofvalue(coodnext,field,fvalue);  //check the next color
			  assign color = fvalue;
			  if (color == 2'b00) begin
					assign color = 2'b11;
					changefield (field,coodnext,color,fieldout);
					field <= fieldout;
			  end
			  Repeat <= Repeat + 4'b1;
		 end
		 if (Count > 0) begin
			  assign color = 2'b10;
			  changefield(field,coodi,color,fieldout);    //change color where put
			  field <= fieldout;
			  sum10 <= sum10 + Count + 1;    // renew the score of '10'
		 end
		 assign turn = 0;
	end
	else begin     //the turn of 01
		 //changing the field when putting the piece

		 Repeat <= 4'b0000;
		 while (Repeat != 4'b1000) begin  // checking for 8 directions
			  nextcood(cood,Repeat,coodout);  //
			  assign coodnext = coodout;
			  xyBIN8tofvalue(coodnext,field,fvalue);  //check the next color
			  assign color = fvalue;  //'color' is the color of the next coodinate
			  vecl <=0;
			  Count <=0;

			  //conditional branch
			  if (color == 2'b10) begin  // keep on checking
					cood <= coodnext;
					vecl <= vecl + 3'b1;
			  end
			  else begin
					if (color == 2'b01 and vecl > 0) begin  // if able to flip
						 cood <= coodi;
						 count <= count + vecl;
						 while (vecl > 0) begin         //
							  nextcood(cood,Repeat,coodout);
							  assign coodnext = coodout;
							  assign color = 2'b01;
							  changefield(field,coodnext,color,fieldout);
							  field <= fieldout;
							  vecl <= vecl - 1;           // changing field
						 end
					end
					Repeat <= Repeat + 4'b1;     // move to the next direction
					cood <= coodi;
					vecl <= 0;
			  end
		 end

		 // changeing the field so as to wait for putting a piece

		 Repeat <= 4'b0000;
		 while (Repeat != 4'b1000) begin
			  nextcood(coodi,Repeat,coodout);  // checking for 8 directions
			  assign coodnext = coodout;
			  xyBIN8tofvalue(coodnext,field,fvalue);  //check the next color
			  assign color = fvalue;
			  if (color == 2'b00) begin
					assign color = 2'b11;
					changefield (field,coodnext,color,fieldout);
					field <= fieldout;
			  end
			  Repeat <= Repeat + 4'b1;
		 end
		 if (Count > 0) begin
			  assign color = 2'b01;
			  changefield(field,coodi,color,fieldout);    //change color where put
			  field <= fieldout;
			  sum01 <= sum01 + Count + 1;    // renew the score of '01'
		 end
		 assign turn = 1;
	end
	end
