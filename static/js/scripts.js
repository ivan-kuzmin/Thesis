$(function () {$('[data-toggle="tooltip"]').tooltip()})

var $input = $(".typeahead");
$input.typeahead({
    source: [
        {id: "1", name: "CQNZ1"},
        {id: "2", name: "RQSN1"},
        {id: "3", name: "RQCN1"},
        {id: "4", name: "RQLN1"},
        {id: "5", name: "RQNZVR"},
        {id: "6", name: "RQLNSQ"},
        {id: "7", name: "CXCT"},
        {id: "8", name: "CXGD1"},
        {id: "9", name: "CXGD2"},
        {id: "10", name: "CXNZ1"},
        {id: "11", name: "CXNZ2"},
        {id: "12", name: "XSPGN1"},
        {id: "13", name: "ASPG"},
        {id: "14", name: "DCXPD"},
        {id: "15", name: "DCXWT"},
        {id: "16", name: "DCXCS"},
        {id: "17", name: "PDGD1"},
        {id: "18", name: "PDGDN1"},
        {id: "19", name: "PDJT1"},
        {id: "20", name: "RXJT1"},
        {id: "21", name: "RXSP1"},
        {id: "22", name: "BLJT1"},
        {id: "23", name: "BLSP1"},
        {id: "24", name: "VBLS"},
        {id: "25", name: "TBLS"}
    ],
    autoSelect: true,
    fitToElement: true,
    autoSelect: false,
    afterSelect: function(item) {
        window.location.href = item.name;
    }
});
