from django.views import View
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView


class WelcomeView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('')


class MenuView(TemplateView):
    menu = {
        'Change oil': 'change_oil',
        'Inflate tires': 'inflate_tires',
        'Diagnostic': 'diagnostic',
    }
    template_name = 'menu/contents.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={'menu': self.menu})


class ChangeOilView(View):
    def get(self, request, *args, **kwargs):
        ticket_type = CurTicketHandler.change_oil_ticket
        html = CurTicketHandler.get_html(ticket_type)
        CurTicketHandler.add_ticket(ticket_type)
        return HttpResponse(html)


class UpdateTiresView(View):
    def get(self, request, *args, **kwargs):
        ticket_type = CurTicketHandler.inflate_tires_ticket
        html = CurTicketHandler.get_html(ticket_type)
        CurTicketHandler.add_ticket(ticket_type)
        return HttpResponse(html)


class DiagnosticView(View):
    def get(self, request, *args, **kwargs):
        ticket_type = CurTicketHandler.diagnostic_ticket
        html = CurTicketHandler.get_html(ticket_type)
        CurTicketHandler.add_ticket(ticket_type)
        return HttpResponse(html)


class ProcessingView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "processing/contents.html",
                      context={'change_oil_ticket': CurTicketHandler.get_change_oil_ticket(),
                               'inflate_tires_ticket': CurTicketHandler.get_inflate_tires_ticket(),
                               'diagnostic_ticket': CurTicketHandler.get_diagnostic_ticket()})

    def post(self, request, *args, **kwargs):
        CurTicketHandler.remove_next_ticket()
        return redirect('/next')


class NextView(View):
    def get(self, request, *args, **kwargs):
        next_ticket = CurTicketHandler.get_next_ticket()
        if next_ticket != -1:
            html = f"<div>Next ticket #{next_ticket}</div>"
        else:
            html = "<div>Waiting for the next client</div>"
        return HttpResponse(html)


class TicketHandler:
    line_of_cars = dict()
    change_oil_ticket = 0
    inflate_tires_ticket = 1
    diagnostic_ticket = 2
    id = 0
    next_ticket = -1

    def __init__(self):
        self.line_of_cars[self.change_oil_ticket] = list()
        self.line_of_cars[self.inflate_tires_ticket] = list()
        self.line_of_cars[self.diagnostic_ticket] = list()

    def get_next_ticket(self):
        return self.next_ticket

    def remove_next_ticket(self):
        if self.line_of_cars[self.change_oil_ticket]:
            self.next_ticket = self.line_of_cars[self.change_oil_ticket].pop(0)
        elif self.line_of_cars[self.inflate_tires_ticket]:
            self.next_ticket = self.line_of_cars[self.inflate_tires_ticket].pop(0)
        elif self.line_of_cars[self.diagnostic_ticket]:
            self.next_ticket = self.line_of_cars[self.diagnostic_ticket].pop(0)
        else:
            self.next_ticket = -1

    def get_next_ticket_num(self):
        return self.id + 1

    def get_wait_time(self, ticket_type):
        wait_time = len(self.line_of_cars[self.change_oil_ticket]) * 2
        if ticket_type == self.change_oil_ticket:
            return wait_time

        wait_time += len(self.line_of_cars[self.inflate_tires_ticket]) * 5
        if ticket_type == self.inflate_tires_ticket:
            return wait_time

        wait_time += len(self.line_of_cars[self.diagnostic_ticket]) * 30
        return wait_time

    def add_ticket(self, ticket_type):
        new_id = self.get_next_ticket_num()
        self.line_of_cars[ticket_type].append(new_id)
        self.id = new_id

    def get_html(self, ticket_type):
        return f'''
        <div>Your number is {self.get_next_ticket_num()}</div>
        <div>Please wait around {self.get_wait_time(ticket_type)} minutes</div>
        '''

    def get_change_oil_ticket(self):
        return len(self.line_of_cars[self.change_oil_ticket])

    def get_inflate_tires_ticket(self):
        return len(self.line_of_cars[self.inflate_tires_ticket])

    def get_diagnostic_ticket(self):
        return len(self.line_of_cars[self.diagnostic_ticket])

CurTicketHandler = TicketHandler()
