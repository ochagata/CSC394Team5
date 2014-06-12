    var canvas, ctx, bTrackCoords = false,
        prevX = 0,
        currX = 0,
        prevY = 0,
        currY = 0,
        currCanvasX = 0,
        currCanvasY = 0,
        dot_flag = false;
        sokgraph_x = [];
        sokgraph_y = [];
        letters = [];
    var mousemove_timeout = null;

    var lineColor = "black",
        lineWidth = 2;

    $(function() {
        canvas = document.getElementById('can');
        ctx = canvas.getContext("2d");
        w = canvas.width;
        h = canvas.height;


        canvas.addEventListener("mousedown", function(e) {
            onKeyDown(e)
        }, false);
        canvas.addEventListener("mouseup", function(e) {
            onKeyUp(e)
        }, false);
        canvas.addEventListener("mouseout", function(e) {
            onKeyUp(e)
        }, false);
        $('.row').each(function()
        {
           var $this = $(this);
            $this.children().each(function()
            {
                var offset = $(this).position();
                var curHeight = $(this).height();
                var curWidth = $(this).width();
                var curTop = offset.top;
                var curLeft = offset.left;
                var centerX = curLeft + (curWidth / 2);
                var centerY = curTop + (curHeight / 2);
                var entry = {
                    letter: $(this).attr('id'),
                    center_x: centerX,
                    center_y: centerY
                }
                letters.push(entry);

            });
        });
    });


    function draw()
    {
        ctx.beginPath();
        ctx.moveTo(prevX, prevY);
        ctx.lineTo(currX, currY);
        ctx.strokeStyle = lineColor;
        ctx.lineWidth = lineWidth;
        ctx.stroke();
        ctx.closePath();
    }

        function onKeyDown(e)
        {
                currX = e.clientX;// - canvas.offsetLeft;
                currY = e.clientY;// - canvas.offsetTop;

                currCanvasX = currX - canvas.offsetLeft;
                currCanvasY = currY - canvas.offsetTop;

                prevX = currX;
                prevY = currY;

                $(".row").each(function () {
                    // alert($(this).attr('id'));
                    var $this = $(this);
                    var nowWidth = $this.outerWidth();
                    var nowHeight = $this.outerHeight();
                    var curLeft = $this.position().left;
                    var curTop = $this.position().top;
                    if (currX < curLeft + nowWidth && currX > curLeft) {
                        if (currY < curTop + nowHeight && currY > curTop) {
                            $this.children().each(function () {
                                var curId = $(this).attr('id');
                                var curOffset = $(this).position();
                                var newLeft = curOffset.left;
                                var newTop = curOffset.top;
                                var newWidth = $(this).outerWidth();
                                var newHeight = $(this).outerHeight();
                                var xCenter = newLeft + (newWidth / 2);
                                var yCenter = newTop + (newHeight / 2);
                                if (currY > yCenter - 50 && currY < yCenter + 50) {
                                    if (currX > xCenter - 50 && currX < xCenter + 50) {
                                        //letters.push($(this).attr('id'));
                                        //alert("Id: " + $(this).attr('id'));
                                    }
                                }
                            });

                        }
                    }
                });

                //the user has clicked, so we should start tracking their mouse movements
                bTrackCoords = true;
                dot_flag = true;
                if (dot_flag) {
                    canvas.addEventListener("mousemove",
                        onKeyMove(e), false);

                    ctx.beginPath();
                    ctx.moveTo(currCanvasX, currCanvasY);
                    ctx.fillStyle = lineColor;
                    ctx.fillRect(currCanvasX, currCanvasY, 2, 2);
                    ctx.closePath();
                    dot_flag = false;
                }
            }
    function onKeyUp(e)
    {
            if(bTrackCoords)
            {
                canvas.removeEventListener("mousemove", onKeyMove);
                setInterval(function(){}, 1000);
                var currentInterval_x = sokgraph_x[sokgraph_x.length - 1];
                //the reference to sokgraph_x intead of sokgraph_y here is intentional
                var currentInterval_y = sokgraph_y[sokgraph_x.length - 1];
                for(var i = sokgraph_x.length - 1; i > 0; i--)
                {
                    if (Math.abs(currentInterval_x - sokgraph_x[i-1]) <= 5)
                    {
                        if(Math.abs(currentInterval_y - sokgraph_y[i-1]) <= 5)
                        {
                            sokgraph_x.splice(i-1, 1);
                            sokgraph_y.splice(i-1, 1);
                        }
                        else
                        {
                            currentInterval_x = sokgraph_x[i-1];
                            currentInterval_y = sokgraph_y[i-1];
                        }

                    }
                    else
                    {
                        currentInterval_x = sokgraph_x[i-1];
                        currentInterval_y = sokgraph_y[i-1];
                    }
                }
//                alert("X values: " + sokgraph_x);
//                alert("Y values: " + sokgraph_y);
//                alert("X values: " + sokgraph_x);
//
//                alert("X length: " + sokgraph_x.length);
//                alert("Y length: " + sokgraph_y.length);

               // alert("Letters: " + letters);
                $.ajax({
                    type:"POST",
                    url: "/ARK/test_ajax/",
                    data: {'x_coords': sokgraph_x, 'y_coords':sokgraph_y, 'letters': letters},
                    dataType: "html",
                    success:function(){alert("ajax hookup successful!");},
                })

                //get the arrays ready to store the next sokgraph and stop tracking their
                //coordinates until they click again
                sokgraph_x = [];
                sokgraph_y = [];
                //letters = [];
                bTrackCoords = false;
                prevX = 0;
                prevY = 0;

            }
            erase();
        }
        function onKeyMove(e)
        {
                if (bTrackCoords)
                {
                    prevX = currX;
                    prevY = currY;
                    currX = e.clientX - canvas.offsetLeft;
                    currY = e.clientY - canvas.offsetTop;
                    sokgraph_x.push(currX);
                    sokgraph_y.push(currY);


                    draw();
//                    if(mousemove_timeout == null)
//                    {
//                        mousemove_timeout = window.setTimeout(realMove, 100);
//                    }
                }
        }

        function realMove()
        {
            prevX = currX;
            prevY = currY;
            currX = e.clientX - canvas.offsetLeft;
            currY = e.clientY - canvas.offsetTop;
            sokgraph_x.push(currX);
            sokgraph_y.push(currY);


            draw();
            window.clearTimeout(mousemove_timeout);
            mousemove_timeout = null;
        }

        function erase()
        {
            ctx.clearRect(0, 0, w, h);
        }