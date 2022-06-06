;(function () {
    const $document = $(document)

    function bindListeners() {
        const attrGoodsUrl = 'data-goods-url';
        const selGoodsUrl = '[' + attrGoodsUrl + ']';

        const attrDismiss = 'data-dismiss'
        const selDismiss = '[' + attrDismiss + ']';

        const $elModalGood = $('#modal-good')
        const $elModalBackdrop = $('.modal-backdrop')
        const $elModalContent = $elModalGood.find('.modal-content')


        $document
            .on('submit', 'form', function (evt) {
                evt.preventDefault()
                const $el = $(this)

                console.log($el)
                console.log($el.serialize())

                $.ajax({
                    type: "POST",
                    url: $el.data('action'),
                    data: new FormData($el.get(0)),
                    cache: false,
                    contentType: false,
                    processData: false,
                })
                    .done(function () {
                        location.reload();
                    })
                    .fail(function (err) {
                        console.error(err)
                    })


                return false;
            })
            .on('click', selDismiss, function () {
                $elModalBackdrop.removeClass('show').hide()
                $elModalGood.removeClass('show').hide()
            })
            .on('click', selGoodsUrl, function () {
                const $el = $(this);
                const url = $el.attr(attrGoodsUrl);

                $.ajax({
                    type: 'get',
                    url: url,
                })
                .done(function(formHTML) {
                    // console.log("done", formHTML);
                    $elModalContent.html(formHTML);
                    $elModalBackdrop.addClass('show').show()
                    $elModalGood.addClass('show').show()
                })
                .fail(function(err) {
                    console.log("fail", err);
                })
                .always(function() {
                    // console.log("always");
                });
            });
    }

    $document.ready(bindListeners);
})()
