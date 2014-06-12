    var canvas, ctx, bTrackCoords = false,
        prevX = 0,
        currX = 0,
        prevY = 0,
        currY = 0,
        dot_flag = false;
        sokgraph_x = [];
        sokgraph_y = [];
        letters = [];

    var lineColor = "black",
        lineWidth = 2;

    $(function() {
        canvas = document.getElementById('can');
        ctx = canvas.getContext("2d");
        w = canvas.width;
        h = canvas.height;

        canvas.addEventListener("mousemove", function(e) {
            findxy('move', e)
        }, false);
        canvas.addEventListener("mousedown", function(e) {
            findxy('down', e)
        }, false);
        canvas.addEventListener("mouseup", function(e) {
            findxy('up', e)
        }, false);
        canvas.addEventListener("mouseout", function(e) {
            findxy('out', e)
        }, false);
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

    function findxy(res, e)
    {
        if (res == 'down')
        {
            currX = e.clientX - canvas.offsetLeft;
            currY = e.clientY - canvas.offsetTop;
            prevX = currX;
            prevY = currY;

            $(".row").each(function(index, element)
            {
                 alert($(this).attr('id'));
                    var $this = $(this);
                    var nowWidth = $this.width();
                    var nowHeight = $this.height();
                    var curOffset = $this.offset;
                    var curLeft = $this.offset().left;
                    var curTop = $this.offset().top;
                    if(currX < curLeft + nowWidth && currX > curLeft)
                    {
                        if(currY < curTop + nowHeight && currY > curTop)
                        {
                            $this.children().each(function()
                            {

                                var curOffset = $(this).offset();
                                var xCenter = curOffset.left + ($(this).width() / 2);
                                var yCenter = curOffset.top + ($(this).height() / 2);
                                if(currY < yCenter - 5 || currY > yCenter + 5 )
                                {
                                    if(currX < xCenter - 5 || currX > xCenter + 5)
                                   {
                                        letters.push($(this).attr('id'));
                                       alert("Id: " + $(this).attr('id'));
                                   }
                                }
                            });

                        }
                    }
            });

            //TODO: make 3 a computed value based on number of rows
//            for(var i = 1; i <= 3; ++i)
//            {
//                var curRow = $('#row' + i);
//                alert("Row class: " + curRow.attr('id'));
//                $.each(curRow, function(index, element)
//                {
//                    alert($(this).attr('id'));
//                    var now = $(this);
//                    var nowWidth = now.width();
//                    var nowHeight = now.height();
//                    var curOffset = now.offset;
//                    var curLeft = now.offset().left;
//                    var curTop = now.offset().top;
//                    if(currX < curLeft + nowWidth && currX > curLeft)
//                    {
//                        if(currY < curTop + nowHeight && currY > curTop)
//                        {
//                            alert("Id: " + now.attr('id'));
//                        var curOffset = now.offset();
//                        var xCenter = curOffset.left + (now.width() / 2);
//                        var yCenter = curOffset.top + (now.height() / 2);
//                        if(currY < yCenter - 5 || currY > yCenter + 5 )
//                        {
//                            if(currX < xCenter - 5 || currX > xCenter + 5)
//                            {
//                                letters.push(now.attr('id'));
//                            }
//                        }
//                        }
//                    }
//
////                    var $this = $(this);
////                    $this.each(function(index, element)
////                    {
////                        var $secondThis = $(this);
////                        alert("Id: " + $secondThis.attr('id'));
////                        var curOffset = $secondThis.offset();
////                        var xCenter = curOffset.left + ($secondThis.width() / 2);
////                        var yCenter = curOffset.top + ($secondThis.height() / 2);
////                        if(currY < yCenter - 5 || currY > yCenter + 5 )
////                        {
////                            if(currX < xCenter - 5 || currX > xCenter + 5)
////                            {
////                                letters.push($secondThis.attr('id'));
////                            }
////                        }
////                    });
//
//                });
//            }

            //when clicking on a point in the canvas, the x value gets pushed here, but the y value gets pushed here and
            //somewhere else
//            sokgraph_x.push(currX);
//            sokgraph_y.push(currY);

            //the user has clicked, so we should start tracking their mouse movements
            bTrackCoords = true;
            dot_flag = true;
            if (dot_flag)
            {
                ctx.beginPath();
                ctx.fillStyle = lineColor;
                ctx.fillRect(currX, currY, 2, 2);
                ctx.closePath();
                dot_flag = false;
            }
        }
        if (res == 'up' || res == "out")
        {
            if(bTrackCoords)
            {
                setInterval(function(){}, 2000);
                alert("X values: " + sokgraph_x);
                alert("Y values: " + sokgraph_y);
                alert("X values: " + sokgraph_x);

                alert("X length: " + sokgraph_x.length);
                alert("Y length: " + sokgraph_y.length);

                alert("Letters: " + letters);

                //get the arrays ready to store the next sokgraph and stop tracking their
                //coordinates until they click again
                sokgraph_x = [];
                sokgraph_y = [];
                bTrackCoords = false;

            }
            erase();
        }
        if (res == 'move')
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
            }
        }

        function erase()
        {
            ctx.clearRect(0, 0, w, h);

            //as is, this throws a TypeError because that element does not exist. If it gets added, we should uncomment this
            //document.getElementById("canvasimg").style.display = "none";

        }
    }